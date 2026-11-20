#!/usr/bin/env python3
import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
BASE = "https://k501-information-space.github.io/AIONARC_CHANNEL/"
HUB = "https://switchboard.p3k.io/"
def main():
    r = json.loads((ROOT / "signals/registry.json").read_text(encoding="utf-8"))
    ss = r["signals"]
    ids = ["AIONARC_SIGNAL_{:04d}".format(i) for i in range(1, 18)]
    assert [s["signal_id"] for s in ss] == ids
    assert len({s["target_url"] for s in ss}) == 17
    assert all(s["channel_page"] == BASE + "signals/" + s["signal_id"] + "/" for s in ss)
    nxt = r["signal_namespace"]["next_slot"]
    assert nxt["signal_id"] == "AIONARC_SIGNAL_0018" and nxt["status"] == "OPEN_UNASSIGNED" and nxt["publish"] is False
    key = (ROOT / "signals/indexnow.key").read_text(encoding="utf-8").strip()
    assert re.fullmatch(r"[A-Za-z0-9-]{8,128}", key)
    assert (ROOT / (key + ".txt")).read_text(encoding="utf-8").strip() == key
    assert not (ROOT / "signals/AIONARC_SIGNAL_0018/index.html").exists()
    for s in ss:
        p = ROOT / "signals" / s["signal_id"] / "index.html"
        assert p.is_file() and s["signal_id"] in p.read_text(encoding="utf-8")
    f = json.loads((ROOT / "feed.json").read_text(encoding="utf-8"))
    assert f["version"] == "https://jsonfeed.org/version/1.1"
    assert len(f["items"]) == 17 and f["hubs"] == [{"type": "WebSub", "url": HUB}]
    assert [i["_k501_signal_id"] for i in f["items"]] == list(reversed(ids))
    assert all(i["url"].startswith(BASE) and i["external_url"].startswith("https://") for i in f["items"])
    rss = ET.parse(ROOT / "rss.xml").getroot()
    assert rss.tag == "rss" and rss.attrib.get("version") == "2.0" and len(rss.findall("./channel/item")) == 17
    atom = ET.parse(ROOT / "atom.xml").getroot()
    ns = "{http://www.w3.org/2005/Atom}"
    assert atom.tag == ns + "feed" and len(atom.findall(ns + "entry")) == 17
    sm = ET.parse(ROOT / "sitemap.xml").getroot()
    urls = [e.text for e in sm.findall("s:url/s:loc", {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"})]
    assert urls == [BASE] + [s["channel_page"] for s in ss]
    assert all(s["target_url"] not in urls for s in ss)
    assert "Sitemap: " + BASE + "sitemap.xml" in (ROOT / "robots.txt").read_text(encoding="utf-8")
    text = (ROOT / "index.html").read_text(encoding="utf-8") + (ROOT / "rss.xml").read_text(encoding="utf-8") + (ROOT / "atom.xml").read_text(encoding="utf-8") + (ROOT / "feed.json").read_text(encoding="utf-8")
    assert not re.search(r"(?<!AIONARC_)SIGNAL_[0-9]{4}", text)
    print("VALIDATION_PASS assigned=17 pages=17 feeds=17 sitemap_urls=18 indexnow_key=PASS websub=PASS")
if __name__ == "__main__":
    main()
