#!/usr/bin/env python3
import json, os, re, subprocess, time
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
BASE = "https://k501-information-space.github.io/AIONARC_CHANNEL/"
FEEDS = ("rss.xml", "atom.xml", "feed.json")
USER_AGENT = "AIONARC_CHANNEL/1.1 (+https://k501-information-space.github.io/AIONARC_CHANNEL/Gateway.md)"
HEADER_ALLOW = ("server", "www-authenticate", "via", "cf-ray", "x-request-id", "x-cache", "location", "retry-after", "content-type")

def request(url, method="GET", data=None, headers=None):
    request_headers = {"User-Agent": USER_AGENT, "Accept": "*/*"}
    request_headers.update(headers or {})
    try:
        with urlopen(Request(url, data=data, headers=request_headers, method=method), timeout=25) as response:
            body = "" if method == "HEAD" else response.read().decode("utf-8", "replace")
            return response.status, body, dict(response.headers.items())
    except HTTPError as error:
        body = "" if method == "HEAD" else error.read().decode("utf-8", "replace")
        return error.code, body, dict(error.headers.items()) if error.headers else {}
    except (URLError, TimeoutError) as error:
        return 0, str(error), {}

def safe_headers(headers):
    values = {str(k).lower(): str(v) for k, v in headers.items()}
    return {k: values[k] for k in HEADER_ALLOW if k in values}

def changed_outputs():
    event_path = os.environ.get("GITHUB_EVENT_PATH")
    if not event_path or not Path(event_path).is_file():
        return [BASE], True
    event = json.loads(Path(event_path).read_text(encoding="utf-8"))
    before = event.get("before")
    after = os.environ.get("GITHUB_SHA") or event.get("after")
    if not before or not after or set(before) == {"0"}:
        return [BASE] + [BASE + "signals/AIONARC_SIGNAL_{:04d}/".format(i) for i in range(1, 18)], True
    diff = subprocess.run(["git", "diff", "--name-status", "--find-renames", before, after], cwd=ROOT, text=True, capture_output=True, check=True).stdout
    urls, feeds_changed = set(), False
    for line in diff.splitlines():
        fields = line.split("\t")
        if len(fields) < 2: continue
        changed_paths = fields[1:] if fields[0].startswith(("R", "C")) else [fields[1]]
        for path in changed_paths:
            if path == "index.html": urls.add(BASE)
            match = re.fullmatch(r"signals/(AIONARC_SIGNAL_[0-9]{4})/index\.html", path)
            if match:
                urls.add(BASE + "signals/" + match.group(1) + "/")
                feeds_changed = True
            if path in FEEDS: feeds_changed = True
    return sorted(urls), feeds_changed

def wait_pages(key, registry_id):
    tests = [(BASE, "AIONARC_SIGNAL_0017"), (BASE+"rss.xml", "AIONARC_SIGNAL_0017"), (BASE+"atom.xml", "AIONARC_SIGNAL_0017"), (BASE+"feed.json", registry_id), (BASE+"sitemap.xml", "AIONARC_SIGNAL_0017"), (BASE+key+".txt", key)]
    for attempt in range(36):
        failures = []
        for url, marker in tests:
            status, body, _ = request(url)
            if status != 200 or marker not in body: failures.append(url + " HTTP " + str(status))
        if not failures:
            print("PAGES_PUBLIC_GET_CHECK_PASS checks=6")
            return
        print("Pages wait {}/36: {}".format(attempt + 1, "; ".join(failures)))
        time.sleep(10)
    raise RuntimeError("New Pages outputs and IndexNow key are not publicly reachable")

def verify_topics():
    observations, errors = {}, []
    for feed in FEEDS:
        status, _, headers = request(BASE + feed, method="HEAD")
        observations[feed] = {"head_status": status, "headers": safe_headers(headers)}
        print("Topic HEAD", feed, "HTTP", status, json.dumps(observations[feed]["headers"], sort_keys=True))
        if status < 200 or status >= 300: errors.append(feed + " HEAD HTTP " + str(status))
    return observations, errors

def send_indexnow(urls, key):
    if not urls: return "SKIPPED_NO_CHANGED_OWNED_HTML_URLS"
    payload = {"host":"k501-information-space.github.io","key":key,"keyLocation":BASE+key+".txt","urlList":urls}
    status, body, headers = request("https://api.indexnow.org/indexnow", "POST", json.dumps(payload).encode("utf-8"), {"Content-Type":"application/json; charset=utf-8"})
    print("IndexNow HTTP", status, "URL count", len(urls), "headers", json.dumps(safe_headers(headers), sort_keys=True))
    if status == 200: return "SUBMISSION_ACCEPTED_HTTP_200"
    if status == 202: return "ACCEPTED_PENDING_KEY_VALIDATION_HTTP_202"
    raise RuntimeError("IndexNow response was not HTTP 200/202: " + str(status) + " " + body[:300])

def publish_websub(feed_changed, topic_observations, hubs):
    results, endpoint_errors = {}, []
    accepted_by_feed = {feed: [] for feed in FEEDS}
    for hub in hubs:
        per_feed = {}
        for feed in FEEDS:
            if not feed_changed:
                per_feed[feed] = {"status":"SKIPPED_FEED_UNCHANGED"}
                continue
            payload = urlencode({"hub.mode":"publish","hub.url":BASE+feed}).encode("utf-8")
            status, body, headers = request(hub, "POST", payload, {"Content-Type":"application/x-www-form-urlencoded"})
            result = {"status":status,"headers":safe_headers(headers),"body_excerpt":body[:300],"topic_head_status":topic_observations.get(feed,{}).get("head_status")}
            per_feed[feed] = result
            print("WebSub", hub, feed, "HTTP", status, "topic_HEAD", result["topic_head_status"], "headers", json.dumps(result["headers"], sort_keys=True), "body", result["body_excerpt"])
            if 200 <= status < 300: accepted_by_feed[feed].append(hub)
            else: endpoint_errors.append(hub + " " + feed + " HTTP " + str(status))
        results[hub] = per_feed
    missing = [feed for feed in FEEDS if feed_changed and not accepted_by_feed[feed]]
    return results, endpoint_errors, accepted_by_feed, missing

def main():
    registry = json.loads((ROOT/"signals/registry.json").read_text(encoding="utf-8"))
    key = (ROOT/"signals/indexnow.key").read_text(encoding="utf-8").strip()
    hubs = registry["distribution"]["websub"]["active_hub_urls"]
    urls, feeds_changed = changed_outputs()
    if not urls and not feeds_changed:
        print("No owned pages or feed changed; skipped")
        return
    wait_pages(key, registry["artifact_id"])
    topics, topic_errors = verify_topics()
    indexnow_result = send_indexnow(urls, key)
    websub_results, endpoint_errors, accepted_by_feed, missing = publish_websub(feeds_changed, topics, hubs)
    report = [
        "AIONARC_CHANNEL post-deployment notification diagnostics",
        "IndexNow: " + indexnow_result,
        "Changed owned HTML URLs: " + str(len(urls)),
        "WebSub hubs configured: " + json.dumps(hubs),
        "WebSub topic HEAD: " + json.dumps(topics, sort_keys=True),
        "WebSub publisher responses: " + json.dumps(websub_results, sort_keys=True),
        "WebSub accepted hubs by feed: " + json.dumps(accepted_by_feed, sort_keys=True),
        "WebSub endpoint errors (non-fatal when another hub accepts): " + json.dumps(endpoint_errors),
        "WebSub topic HEAD errors: " + json.dumps(topic_errors),
        "WebSub feeds without any accepted hub: " + json.dumps(missing),
        "Publisher acknowledgement is not subscriber-delivery proof.",
        "IndexNow receipt is not indexing proof.",
        "External targets were excluded from IndexNow."
    ]
    summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary_path: Path(summary_path).write_text("\n".join(report) + "\n", encoding="utf-8")
    print("POST_DEPLOYMENT_NOTIFICATION_DIAGNOSTICS_COMPLETE")
    if topic_errors or missing:
        raise RuntimeError("No configured WebSub hub accepted every changed feed: " + json.dumps(topic_errors + missing))
    if endpoint_errors: print("WEBSUB_SECONDARY_ENDPOINT_ERRORS_RECORDED_NON_FATAL")

if __name__ == "__main__":
    main()
