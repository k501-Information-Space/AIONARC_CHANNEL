#!/usr/bin/env python3
import json
import os
import re
import subprocess
import time
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen
ROOT = Path(__file__).resolve().parents[1]
BASE = "https://k501-information-space.github.io/AIONARC_CHANNEL/"
HUB = "https://switchboard.p3k.io/"
FEEDS = ("rss.xml", "atom.xml", "feed.json")
def request(url, method="GET", data=None, headers=None):
    try:
        with urlopen(Request(url, data=data, headers=headers or {}, method=method), timeout=20) as response:
            return response.status, response.read().decode("utf-8", "replace")
    except HTTPError as exc:
        return exc.code, exc.read().decode("utf-8", "replace")
    except (URLError, TimeoutError) as exc:
        return 0, str(exc)
def changed():
    ep = os.environ.get("GITHUB_EVENT_PATH")
    if not ep or not Path(ep).is_file():
        return [BASE], True
    event = json.loads(Path(ep).read_text(encoding="utf-8"))
    before = event.get("before")
    after = os.environ.get("GITHUB_SHA") or event.get("after")
    if not before or not after or set(before) == {"0"}:
        return [BASE] + [BASE + "signals/AIONARC_SIGNAL_{:04d}/".format(i) for i in range(1, 18)], True
    diff = subprocess.run(["git", "diff", "--name-status", "--find-renames", before, after],
                          cwd=ROOT, text=True, capture_output=True, check=True).stdout
    urls, feed_changed = set(), False
    for line in diff.splitlines():
        fields = line.split("\t")
        if len(fields) < 2:
            continue
        paths = fields[1:] if fields[0].startswith(("R", "C")) else [fields[1]]
        for path in paths:
            if path == "index.html":
                urls.add(BASE)
            match = re.fullmatch(r"signals/(AIONARC_SIGNAL_[0-9]{4})/index\.html", path)
            if match:
                urls.add(BASE + "signals/" + match.group(1) + "/")
                feed_changed = True
            if path in FEEDS:
                feed_changed = True
    return sorted(urls), feed_changed
def wait_pages(key, registry_id):
    checks = [
        (BASE, "AIONARC_SIGNAL_0017"), (BASE + "rss.xml", "AIONARC_SIGNAL_0017"),
        (BASE + "atom.xml", "AIONARC_SIGNAL_0017"), (BASE + "feed.json", registry_id),
        (BASE + "sitemap.xml", "AIONARC_SIGNAL_0017"), (BASE + key + ".txt", key)
    ]
    for attempt in range(1, 37):
        failed = []
        for url, marker in checks:
            status, body = request(url)
            if status != 200 or marker not in body:
                failed.append(url + " HTTP " + str(status))
        if not failed:
            return
        print("Pages readiness {}/36: {}".format(attempt, "; ".join(failed)))
        time.sleep(10)
    raise RuntimeError("Expected Pages outputs and IndexNow key did not become publicly reachable.")
def indexnow(urls, key):
    if not urls:
        return "SKIPPED_NO_CHANGED_OWNED_HTML_URLS"
    payload = {"host": "k501-information-space.github.io", "key": key,
               "keyLocation": BASE + key + ".txt", "urlList": urls}
    data = json.dumps(payload).encode("utf-8")
    for attempt in range(1, 4):
        status, body = request("https://api.indexnow.org/indexnow", "POST", data,
                               {"Content-Type": "application/json; charset=utf-8"})
        print("IndexNow attempt {}: HTTP {}, URLs={}".format(attempt, status, len(urls)))
        if status == 200:
            return "SUBMISSION_ACCEPTED_HTTP_200"
        if status == 202:
            return "ACCEPTED_PENDING_KEY_VALIDATION_HTTP_202"
        if status not in (0, 429):
            raise RuntimeError("IndexNow rejected request: HTTP {} {}".format(status, body[:400]))
        time.sleep(30 * attempt)
    raise RuntimeError("IndexNow did not return HTTP 200 or 202 after bounded retries.")
def websub(feed_changed):
    results = {}
    for feed in FEEDS:
        if not feed_changed:
            results[feed] = "SKIPPED_FEED_UNCHANGED"
            continue
        data = urlencode({"hub.mode": "publish", "hub.url": BASE + feed}).encode("utf-8")
        status, body = request(HUB, "POST", data, {"Content-Type": "application/x-www-form-urlencoded"})
        print("Switchboard {}: HTTP {}".format(feed, status))
        if status < 200 or status >= 300:
            raise RuntimeError("Switchboard rejected {}: HTTP {} {}".format(feed, status, body[:400]))
        results[feed] = "PUBLISH_REQUEST_ACCEPTED_HTTP_{}".format(status)
    return results
def main():
    r = json.loads((ROOT / "signals/registry.json").read_text(encoding="utf-8"))
    key = (ROOT / "signals/indexnow.key").read_text(encoding="utf-8").strip()
    urls, feed_changed = changed()
    if not urls and not feed_changed:
        print("No owned pages or feeds changed; notifications skipped.")
        return
    wait_pages(key, r["artifact_id"])
    ix = indexnow(urls, key)
    ws = websub(feed_changed)
    report = [
        "# AIONARC_CHANNEL notification result", "",
        "IndexNow: " + ix,
        "Owned HTML URLs submitted: " + str(len(urls)),
        "Switchboard: " + json.dumps(ws, sort_keys=True),
        "",
        "IndexNow receipt is not proof of crawling or indexing.",
        "Switchboard acceptance is not proof of subscriber delivery or processing.",
        "External target URLs were not submitted to IndexNow."
    ]
    p = os.environ.get("GITHUB_STEP_SUMMARY")
    if p:
        Path(p).write_text("\n".join(report) + "\n", encoding="utf-8")
    print("POST_DEPLOYMENT_NOTIFICATIONS_COMPLETE")
if __name__ == "__main__":
    main()
