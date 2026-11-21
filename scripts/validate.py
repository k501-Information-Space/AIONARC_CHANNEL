#!/usr/bin/env python3
import ast, html, json, re
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = "https://k501-information-space.github.io/AIONARC_CHANNEL/"
HUBS = ["https://pubsubhubbub.appspot.com/", "https://switchboard.p3k.io/"]
EXPECTED = {
    "AIONARC_SIGNAL_0002": ("https://github.com/k501-Information-Space", "K501 Information Space — GitHub Organization"),
    "AIONARC_SIGNAL_0003": ("https://mastodon.social/@K501", "K501 — Mastodon / Fediverse Profile"),
    "AIONARC_SIGNAL_0004": ("https://dev.to/k501is", "Iinkognit0 — DEV Community Profile"),
    "AIONARC_SIGNAL_0006": ("https://www.tiktok.com/@patrick.sayzso", "Patrick Sayzso — TikTok (Historical Creative Channel)"),
    "AIONARC_SIGNAL_0007": ("https://substack.com/@k501is", "Patrick Robert Miller — K501 Substack")
}
def title(s): return s.get("channel_display_title") or s.get("verified_source_title")
def main():
    ast.parse((ROOT/"scripts/notify.py").read_text(encoding="utf-8"), filename="scripts/notify.py")
    ast.parse((ROOT/"scripts/websubhub_probe.py").read_text(encoding="utf-8"), filename="scripts/websubhub_probe.py")
    r=json.loads((ROOT/"signals/registry.json").read_text(encoding="utf-8"))
    ss=r["signals"]; ids=["AIONARC_SIGNAL_{:04d}".format(i) for i in range(1,18)]
    assert [s["signal_id"] for s in ss]==ids and len({s["target_url"] for s in ss})==17
    assert all(s["channel_page"]==BASE+"signals/"+s["signal_id"]+"/" for s in ss)
    hubs=r["distribution"]["websub"]["active_hub_urls"]
    assert hubs==HUBS and r["distribution"]["websub"]["hub_url"]==HUBS[0]
    assert r["distribution"]["websub"]["previously_selected_hub_url"]==HUBS[1]
    assert r["distribution"]["websub"]["subscriber_delivery_status"]=="OPEN_NOT_VERIFIED"
    n=r["signal_namespace"]["next_slot"]
    assert n["signal_id"]=="AIONARC_SIGNAL_0018" and n["status"]=="OPEN_UNASSIGNED" and n["publish"] is False
    assert not (ROOT/"signals/AIONARC_SIGNAL_0018/index.html").exists()
    by={s["signal_id"]:s for s in ss}
    for sid,(url,label) in EXPECTED.items():
        s=by[sid];assert s["target_url"]==url and s["channel_display_title"]==label and s["channel_description"].strip()
        assert s["channel_display_title_status"]=="OPERATOR_CONFIRMED_DERIVED_CHANNEL_LABEL"
        assert s["channel_description_status"].startswith("OPERATOR_CONFIRMED")
        assert s["channel_metadata_update_anchor"]["unix_epoch"]==1795249183
    assert by["AIONARC_SIGNAL_0002"]["verified_source_title"]=="k501-Information-Space"
    assert by["AIONARC_SIGNAL_0003"]["verified_source_description"] is None
    assert by["AIONARC_SIGNAL_0004"]["verified_source_description"].startswith("Patrick R. Miller (Iinkognit0)")
    assert by["AIONARC_SIGNAL_0006"]["verified_source_description"]=="Pop-Art Videography and Urbanism"
    assert by["AIONARC_SIGNAL_0007"]["verified_source_description"] is None
    key=(ROOT/"signals/indexnow.key").read_text().strip()
    assert re.fullmatch(r"[A-Za-z0-9-]{8,128}",key)
    key_path=r["distribution"]["indexnow"]["key_file"].rsplit("/",1)[-1]
    assert (ROOT/key_path).read_text().strip()==key
    for s in ss:
        p=html.unescape((ROOT/"signals"/s["signal_id"]/"index.html").read_text(encoding="utf-8"))
        assert s["signal_id"] in p and s["target_url"] in p and title(s) in p
        assert (s.get("channel_description") or s.get("verified_source_description") or "") in p
        assert p.count('rel="hub"')==len(HUBS)
    assert (ROOT/"index.html").read_text().count('rel="hub"')==len(HUBS)
    f=json.loads((ROOT/"feed.json").read_text(encoding="utf-8"))
    assert f["version"]=="https://jsonfeed.org/version/1.1" and f["hubs"]==[{"type":"WebSub","url":u} for u in HUBS] and len(f["items"])==17
    assert [i["_k501_signal_id"] for i in f["items"]]==list(reversed(ids))
    assert f["_k501_metadata_update_anchor"]["unix_epoch"]==1795249183
    for i in f["items"]:
        s=by[i["_k501_signal_id"]]
        assert i["title"]==title(s) and i["url"]==s["channel_page"] and i["external_url"]==s["target_url"]
        assert (s.get("channel_description") or s.get("verified_source_description") or "") in i["content_text"]
    rss=ET.parse(ROOT/"rss.xml").getroot()
    assert rss.tag=="rss" and len(rss.findall("./channel/item"))==17
    rss_hubs=rss.findall("./channel/{http://www.w3.org/2005/Atom}link")
    assert [v.attrib.get("href") for v in rss_hubs if v.attrib.get("rel")=="hub"]==HUBS
    for i in rss.findall("./channel/item"):
        s=next(v for v in ss if v["channel_page"]==i.findtext("link"))
        assert i.findtext("title")==title(s) and i.findtext("guid")==s["channel_page"]
        assert i.find("source").attrib["url"]==s["target_url"]
    ns="{http://www.w3.org/2005/Atom}"
    atom=ET.parse(ROOT/"atom.xml").getroot()
    assert atom.tag==ns+"feed" and len(atom.findall(ns+"entry"))==17
    assert [v.attrib.get("href") for v in atom.findall(ns+"link") if v.attrib.get("rel")=="hub"]==HUBS
    for e in atom.findall(ns+"entry"):
        s=next(v for v in ss if v["channel_page"]==e.findtext(ns+"id"))
        assert e.findtext(ns+"title")==title(s)
        assert s["target_url"] in [v.attrib.get("href") for v in e.findall(ns+"link") if v.attrib.get("rel")=="related"]
    sm=ET.parse(ROOT/"sitemap.xml").getroot()
    locs=[e.text for e in sm.findall("s:url/s:loc",{"s":"http://www.sitemaps.org/schemas/sitemap/0.9"})]
    assert locs==[BASE]+[s["channel_page"] for s in ss] and all(s["target_url"] not in locs for s in ss)
    assert "Sitemap: "+BASE+"sitemap.xml" in (ROOT/"robots.txt").read_text()
    print("VALIDATION_PASS assigned=17 pages=17 feeds=17 metadata=5 sitemap=18 websub_hubs=2 google_primary=PASS switchboard_secondary_retained=OPEN subscriber_delivery=OPEN")
if __name__=="__main__":main()
