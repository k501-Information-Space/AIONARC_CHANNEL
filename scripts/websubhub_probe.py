#!/usr/bin/env python3
"""One-time compatibility probe for an alternate public WebSub hub."""
import sys
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

HUB = "https://websubhub.com/hub"
BASE = "https://k501-information-space.github.io/AIONARC_CHANNEL/"
FEEDS = ("rss.xml", "atom.xml", "feed.json")
USER_AGENT = "AIONARC_CHANNEL-WebSubHub-Probe/1.0 (+https://k501-information-space.github.io/AIONARC_CHANNEL/Gateway.md)"

def probe(topic):
    data = urlencode({"hub.mode": "publish", "hub.topic": topic}).encode("utf-8")
    request = Request(
        HUB,
        data=data,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "*/*",
            "Content-Type": "application/x-www-form-urlencoded",
        },
        method="POST",
    )
    try:
        with urlopen(request, timeout=25) as response:
            body = response.read().decode("utf-8", "replace")
            headers = dict(response.headers.items())
            status = response.status
    except HTTPError as error:
        body = error.read().decode("utf-8", "replace")
        headers = dict(error.headers.items()) if error.headers else {}
        status = error.code
    except (URLError, TimeoutError) as error:
        print("WebSubHub", topic, "NETWORK_ERROR", str(error))
        return 0
    selected = {
        key: value for key, value in headers.items()
        if key.lower() in {
            "server", "content-type", "www-authenticate", "location",
            "retry-after", "via", "x-request-id"
        }
    }
    print(
        "WebSubHub", topic,
        "HTTP", status,
        "headers", selected,
        "body", body[:300]
    )
    return status

def main():
    failures = []
    for feed in FEEDS:
        status = probe(BASE + feed)
        if status < 200 or status >= 300:
            failures.append(feed + " HTTP " + str(status))
    print("WEBSUBHUB_PROBE_COMPLETE", "accepted=3" if not failures else "failures="+", ".join(failures))
    if failures:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
