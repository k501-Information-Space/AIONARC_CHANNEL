#!/usr/bin/env python3
"""Bounded compatibility probes for public WebSub publisher endpoints."""
import json
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

BASE = "https://k501-information-space.github.io/AIONARC_CHANNEL/"
FEEDS = ("rss.xml", "atom.xml", "feed.json")
UA = "AIONARC_CHANNEL-WebSub-Publisher-Probe/1.1 (+https://k501-information-space.github.io/AIONARC_CHANNEL/Gateway.md)"
HEADER_ALLOW = {"server", "content-type", "www-authenticate", "location", "retry-after", "via", "x-request-id", "x-cache"}

PROBES = (
    ("Switchboard underscore alias", "https://switchboard.p3k.io/", "hub_mode", "hub_url", ("rss.xml",)),
    ("WebSubHub", "https://websubhub.com/hub", "hub.mode", "hub.topic", FEEDS),
    ("Google PubSubHubbub", "https://pubsubhubbub.appspot.com/", "hub.mode", "hub.url", FEEDS),
    ("Superfeedr public hub", "https://websub.superfeedr.com/", "hub.mode", "hub.url", FEEDS),
)

def send(label, endpoint, mode_key, topic_key, feed):
    topic = BASE + feed
    payload = urlencode({mode_key: "publish", topic_key: topic}).encode("utf-8")
    request = Request(
        endpoint,
        data=payload,
        headers={
            "User-Agent": UA,
            "Accept": "*/*",
            "Content-Type": "application/x-www-form-urlencoded",
        },
        method="POST",
    )
    try:
        with urlopen(request, timeout=25) as response:
            status = response.status
            body = response.read().decode("utf-8", "replace")
            headers = dict(response.headers.items())
    except HTTPError as error:
        status = error.code
        body = error.read().decode("utf-8", "replace")
        headers = dict(error.headers.items()) if error.headers else {}
    except (URLError, TimeoutError) as error:
        status, body, headers = 0, str(error), {}

    selected = {k: v for k, v in headers.items() if k.lower() in HEADER_ALLOW}
    print(json.dumps({
        "hub": label,
        "endpoint": endpoint,
        "feed": feed,
        "topic": topic,
        "http_status": status,
        "accepted_2xx": 200 <= status < 300,
        "headers": selected,
        "body_excerpt": body[:300],
    }, ensure_ascii=False, sort_keys=True))

def main():
    print("AIONARC_CHANNEL_WEB_SUB_HUB_COMPATIBILITY_PROBE")
    for label, endpoint, mode_key, topic_key, feeds in PROBES:
        for feed in feeds:
            send(label, endpoint, mode_key, topic_key, feed)
    print("PROBE_COMPLETE; HTTP status is a publisher acknowledgement only, not subscriber-delivery proof.")

if __name__ == "__main__":
    main()
