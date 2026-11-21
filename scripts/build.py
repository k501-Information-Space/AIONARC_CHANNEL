#!/usr/bin/env python3
"""Deterministic AIONARC_CHANNEL projection builder; --check compares output bytes."""
import argparse, datetime as dt, html, json, re
from pathlib import Path
from xml.sax.saxutils import escape as xml_escape

ROOT = Path(__file__).resolve().parents[1]
BASE = "https://k501-information-space.github.io/AIONARC_CHANNEL/"

def h(v): return html.escape(str(v if v is not None else ""), quote=True)
def x(v): return xml_escape(str(v if v is not None else ""), {'"': "&quot;", "'": "&apos;"})
def title(s): return s.get("channel_display_title") or s.get("verified_source_title") or s["signal_id"] + " — Source title not supplied or observed"
def desc(s): return s.get("channel_description") or s.get("verified_source_description") or "Source description OPEN; only the operator-supplied target URL is registered."
def summary(s):
    parts = [desc(s)]
    st = s.get("verified_source_title")
    if st and st != title(s): parts.append("Observed source title: " + st + ".")
    sd = s.get("verified_source_description")
    if sd and s.get("channel_description") and sd != s["channel_description"]:
        parts.append("Previously observed source profile description: " + sd + ".")
    parts.extend(["External target: " + s["target_url"], "Channel registration: " + s["channel_registration_time"], "Source publication date: " + (s.get("source_publication_date") or "not asserted"), "Registration is not proof of the external source."])
    return " ".join(parts)

def build():
    r = json.loads((ROOT / "signals/registry.json").read_text(encoding="utf-8"))
    ss = sorted(r["signals"], key=lambda s: s["sequence_number"])
    hubs = r["distribution"]["websub"]["active_hub_urls"]
    ids = ["AIONARC_SIGNAL_{:04d}".format(i) for i in range(1, 18)]
    if [s["signal_id"] for s in ss] != ids or len({s["target_url"] for s in ss}) != 17:
        raise ValueError("Registry sequence or target URLs invalid")
    if not hubs or len(set(hubs)) != len(hubs):
        raise ValueError("WebSub hub list invalid")
    key = (ROOT / "signals/indexnow.key").read_text(encoding="utf-8").strip()
    if not re.fullmatch(r"[A-Za-z0-9-]{8,128}", key):
        raise ValueError("IndexNow key invalid")
    reg = r["registration_time"]
    updated = r["updated_at"]
    updated_dt = dt.datetime.fromisoformat(updated.replace("Z", "+00:00"))
    updated_rfc = updated_dt.strftime("%a, %d %b %Y %H:%M:%S GMT")
    hub_html = "".join('<link rel="hub" href="' + h(u) + '">' for u in hubs)
    o = {}
    home = [
        "<!doctype html>",
        '<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">',
        "<title>AIONARC_CHANNEL — Public Reference Register</title>",
        '<meta name="description" content="AIONARC_CHANNEL public reference register with 17 operator-bound destinations and machine-readable feeds.">',
        '<link rel="canonical" href="' + BASE + '">',
        '<link rel="alternate" type="application/rss+xml" href="' + BASE + 'rss.xml">',
        '<link rel="alternate" type="application/atom+xml" href="' + BASE + 'atom.xml">',
        '<link rel="alternate" type="application/feed+json" href="' + BASE + 'feed.json">',
        hub_html + "</head><body>",
        "<h1>AIONARC_CHANNEL</h1>",
        "<p>Public reference and distribution channel for selected K501 Information Space sources. Not the canonical K501 Information Space.</p>",
        "<p>Active namespace: AIONARC_SIGNAL_NNNN · Assigned: 17 · Latest: AIONARC_SIGNAL_0017</p>",
        "<p>Next slot: AIONARC_SIGNAL_0018 — OPEN / UNASSIGNED / NOT PUBLISHED</p>",
        "<p>Registry anchor: " + str(reg["unix_epoch"]) + " · " + reg["utc"] + "</p>",
        "<p>Channel registration time is not source publication time. Missing metadata remains OPEN or UNKNOWN. The old SIGNAL_NNNN generation is historical and is not remapped.</p>",
        "<h2>Feeds</h2>",
        '<p><a href="' + BASE + 'rss.xml">RSS 2.0</a> · <a href="' + BASE + 'atom.xml">Atom 1.0</a> · <a href="' + BASE + 'feed.json">JSON Feed 1.1</a> · <a href="' + BASE + 'sitemap.xml">Sitemap</a> · <a href="' + BASE + 'robots.txt">robots.txt</a></p>',
        "<p>WebSub hubs: " + " · ".join(hubs) + "</p>",
        "<h2>Registered references</h2><ol>"
    ]
    for s in reversed(ss):
        home.append('<li><a href="' + h(s["channel_page"]) + '">' + h(s["signal_id"]) + "</a> — " + h(title(s)) + ' — <a href="' + h(s["target_url"]) + '">external source</a></li>')
    home.extend(["</ol>", "</body></html>"])
    o["index.html"] = "\n".join(home) + "\n"
    for s in ss:
        t, d = title(s), desc(s)
        p = [
            "<!doctype html>",
            '<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">',
            "<title>" + h(s["signal_id"]) + " — " + h(t) + "</title>",
            '<meta name="description" content="' + h(d) + '">',
            '<link rel="canonical" href="' + h(s["channel_page"]) + '">',
            '<link rel="alternate" type="application/rss+xml" href="' + BASE + 'rss.xml">',
            '<link rel="alternate" type="application/atom+xml" href="' + BASE + 'atom.xml">',
            '<link rel="alternate" type="application/feed+json" href="' + BASE + 'feed.json">',
            hub_html + "</head><body>",
            '<p><a href="' + BASE + '">AIONARC_CHANNEL</a> / Signal reference</p>',
            "<h1>" + h(s["signal_id"]) + "</h1>",
            "<h2>" + h(t) + "</h2>",
            "<p>Status: REGISTERED_REFERENCE · " + h(s["source_title_status"]) + "</p>",
            '<p><a href="' + h(s["target_url"]) + '" rel="external noopener">' + h(s["target_url"]) + "</a></p>",
            "<p>" + h(d) + "</p>"
        ]
        st = s.get("verified_source_title")
        if st and st != t: p.append("<p>Observed source title: " + h(st) + "</p>")
        sd = s.get("verified_source_description")
        if sd and s.get("channel_description") and sd != s["channel_description"]:
            p.append("<p>Previously observed source profile description: " + h(sd) + "</p>")
        p.extend(["<p>Reference kind: " + h(s["reference_kind"]) + "</p>", "<p>Source title status: " + h(s["source_title_status"]) + "</p>", "<p>Source description status: " + h(s["source_description_status"]) + "</p>"])
        if s.get("channel_description_status"): p.append("<p>Channel description status: " + h(s["channel_description_status"]) + "</p>")
        if s.get("channel_display_title_status"): p.append("<p>Channel display title status: " + h(s["channel_display_title_status"]) + "</p>")
        if s.get("source_publication_date"):
            p.append("<p>Source publication date: " + h(s["source_publication_date"]) + " (" + h(s.get("source_version") or "version not supplied") + ", " + h(s.get("source_resource_type") or "type not supplied") + ")</p>")
        else: p.append("<p>Source publication date: Not asserted; channel registration time is not the source publication date.</p>")
        p.extend(["<p>Channel registration time: " + h(s["channel_registration_time"]) + "; anchor " + str(reg["unix_epoch"]) + "</p>", "<p>Source observation scope: " + h(s.get("source_observation", {}).get("scope") or "Scope not separately recorded.") + "</p>", "<h2>Identity and evidence boundary</h2>", "<p>This page is an AIONARC_CHANNEL reference registration. Its URL is the channel permalink; the external target URL remains a separate source reference. Registration does not prove source claims or establish canonical status.</p>", "<p>Missing metadata remains OPEN. External source publication dates are distinct from channel registration time.</p>", "<footer>PROOF_BEFORE_STATE · UNKNOWN_BY_DEFAULT · DERIVED_IS_NOT_CANONICAL</footer>", "</body></html>"])
        o["signals/" + s["signal_id"] + "/index.html"] = "\n".join(p) + "\n"
    rss = ['<?xml version="1.0" encoding="UTF-8"?>', '<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">', "<channel>", "<title>AIONARC_CHANNEL</title>", "<link>" + BASE + "</link>", "<description>Operator-bound reference register; registration does not validate source claims.</description>", "<language>en</language>", "<lastBuildDate>" + updated_rfc + "</lastBuildDate>", '<atom:link href="' + BASE + 'rss.xml" rel="self" type="application/rss+xml"/>']
    rss.extend('<atom:link href="' + x(u) + '" rel="hub"/>' for u in hubs)
    for s in reversed(ss):
        rss.extend(["<item>", "<title>" + x(title(s)) + "</title>", "<link>" + x(s["channel_page"]) + "</link>", '<guid isPermaLink="true">' + x(s["channel_page"]) + "</guid>", "<description>" + x(summary(s)) + "</description>", "<pubDate>" + x(reg["rfc822"]) + "</pubDate>", "<category>" + x(s["reference_kind"]) + "</category>", '<source url="' + x(s["target_url"]) + '">External source reference</source>', "</item>"])
    rss.extend(["</channel>", "</rss>"])
    o["rss.xml"] = "\n".join(rss) + "\n"
    atom = ['<?xml version="1.0" encoding="UTF-8"?>', '<feed xmlns="http://www.w3.org/2005/Atom">', "<title>AIONARC_CHANNEL</title>", "<id>" + BASE + "</id>", '<link href="' + BASE + '" rel="alternate"/>', '<link href="' + BASE + 'atom.xml" rel="self" type="application/atom+xml"/>']
    atom.extend('<link href="' + h(u) + '" rel="hub"/>' for u in hubs)
    atom.extend(["<updated>" + updated + "</updated>", "<subtitle>Operator-bound reference register; registration does not validate source claims.</subtitle>", "<author><name>K501 Information Space</name></author>"])
    for s in reversed(ss):
        atom.extend(["<entry>", "<title>" + x(title(s)) + "</title>", "<id>" + x(s["channel_page"]) + "</id>", '<link href="' + h(s["channel_page"]) + '" rel="alternate"/>', '<link href="' + h(s["target_url"]) + '" rel="related"/>', "<updated>" + updated + "</updated>", "<published>" + x(s["channel_registration_time"]) + "</published>", "<summary>" + x(summary(s)) + "</summary>", '<category term="' + h(s["reference_kind"]) + '"/>', "</entry>"])
    atom.append("</feed>")
    o["atom.xml"] = "\n".join(atom) + "\n"
    items = []
    for s in reversed(ss):
        item = {"id": s["channel_page"], "url": s["channel_page"], "external_url": s["target_url"], "title": title(s), "content_text": summary(s), "date_published": s["channel_registration_time"], "date_modified": s.get("channel_metadata_update_anchor", {}).get("utc", s["channel_registration_time"]), "_k501_signal_id": s["signal_id"], "_k501_reference_kind": s["reference_kind"], "_k501_title_status": s["source_title_status"], "_k501_description_status": s["source_description_status"], "_k501_source_publication_date": s.get("source_publication_date")}
        if s.get("verified_source_title"): item["_k501_source_title"] = s["verified_source_title"]
        if s.get("channel_display_title_status"): item["_k501_channel_display_title_status"] = s["channel_display_title_status"]
        if s.get("channel_description_status"): item["_k501_channel_description_status"] = s["channel_description_status"]
        items.append(item)
    feed = {"version": "https://jsonfeed.org/version/1.1", "title": "AIONARC_CHANNEL", "home_page_url": BASE, "feed_url": BASE + "feed.json", "description": "Operator-bound reference register; registration does not validate source claims.", "language": "en", "authors": [{"name": "K501 Information Space"}], "hubs": [{"type": "WebSub", "url": u} for u in hubs], "items": items, "_k501_registry_anchor": reg["unix_epoch"], "_k501_registry_id": r["artifact_id"], "_k501_active_identifier_namespace": r["signal_namespace"]["active"], "_k501_metadata_update_anchor": r["metadata_update_anchor"]}
    o["feed.json"] = json.dumps(feed, ensure_ascii=False, indent=2) + "\n"
    o["robots.txt"] = "User-agent: *\nAllow: /\nSitemap: " + BASE + "sitemap.xml\n"
    sitemap = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">', "<url><loc>" + x(BASE) + "</loc><lastmod>" + updated[:10] + "</lastmod></url>"]
    for s in ss:
        last = s.get("channel_metadata_update_anchor", {}).get("utc", s["channel_registration_time"])[:10]
        sitemap.append("<url><loc>" + x(s["channel_page"]) + "</loc><lastmod>" + last + "</lastmod></url>")
    sitemap.append("</urlset>")
    o["sitemap.xml"] = "\n".join(sitemap) + "\n"
    key_path = r["distribution"]["indexnow"]["key_file"].rsplit("/", 1)[-1]
    o[key_path] = key + "\n"
    return o

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    outputs = build()
    if args.check:
        missing, mismatched = [], []
        for path, expected in outputs.items():
            target = ROOT / path
            if not target.is_file(): missing.append(path)
            elif target.read_bytes() != expected.encode("utf-8"): mismatched.append(path)
        if missing: print("BUILD_CHECK_MISSING=" + ",".join(sorted(missing)))
        if mismatched: print("BUILD_CHECK_MISMATCH=" + ",".join(sorted(mismatched)))
        if missing or mismatched: raise SystemExit(1)
        print("BUILD_CHECK_PASS outputs_byte_equal=" + str(len(outputs)))
        return
    for path, content in outputs.items():
        target = ROOT / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8", newline="\n")
    print("BUILD_WRITE_PASS outputs=" + str(len(outputs)))

if __name__ == "__main__":
    main()
