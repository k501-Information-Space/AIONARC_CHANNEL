#!/usr/bin/env python3
import argparse
import html
import json
import re
from pathlib import Path
from xml.sax.saxutils import escape as xe

ROOT = Path(__file__).resolve().parents[1]
BASE = "https://k501-information-space.github.io/AIONARC_CHANNEL/"
HUB = "https://switchboard.p3k.io/"

def h(v):
    return html.escape(str(v if v is not None else ""), quote=True)

def x(v):
    return xe(str(v if v is not None else ""))

def read_state():
    r = json.loads((ROOT / "signals/registry.json").read_text(encoding="utf-8"))
    k = (ROOT / "signals/indexnow.key").read_text(encoding="utf-8").strip()
    if not re.fullmatch(r"[A-Za-z0-9-]{8,128}", k):
        raise ValueError("Invalid IndexNow key")
    if len(r["signals"]) != 17:
        raise ValueError("Expected exactly 17 assigned references")
    return r, r["signals"], k

def title(s):
    return s.get("verified_source_title") or s["signal_id"] + " — Source title not supplied or observed"

def description(s):
    return s.get("verified_source_description") or (
        "The operator supplied this target URL for the channel register. "
        "A source title or description has not been supplied or retrieved. "
        "This entry registers the destination only and does not assert source contents."
    )

def summary(s, r):
    return description(s) + " External target: " + s["target_url"] + \
        " Channel registration: " + r["registration_time"]["utc"] + \
        ". Source publication date: " + (s.get("source_publication_date") or "not asserted") + \
        ". Registration is not proof of the external source."

def detail(s, r):
    d = "<p>" + h(s["verified_source_description"]) + "</p>" if s.get("verified_source_description") \
        else "<p>Description status: OPEN. No source description is published as fact.</p>"
    if s.get("source_publication_date"):
        date = s["source_publication_date"] + " (" + (s.get("source_version") or "version not specified")
        if s.get("source_resource_type"):
            date += ", " + s["source_resource_type"]
        date += ")"
    else:
        date = "Not asserted; channel registration time is not the source publication date."
    lines = [
        "<!doctype html>",
        '<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">',
        "<title>" + h(s["signal_id"]) + " — " + h(title(s)) + "</title>",
        '<meta name="description" content="' + h(description(s)[:300]) + '">',
        '<link rel="canonical" href="' + h(s["channel_page"]) + '">',
        '<link rel="alternate" type="application/rss+xml" href="' + BASE + 'rss.xml">',
        '<link rel="alternate" type="application/atom+xml" href="' + BASE + 'atom.xml">',
        '<link rel="alternate" type="application/feed+json" href="' + BASE + 'feed.json">',
        '<link rel="hub" href="' + HUB + '"></head><body>',
        '<p><a href="' + BASE + '">AIONARC_CHANNEL</a> / Signal reference</p>',
        "<h1>" + h(s["signal_id"]) + "</h1>",
        "<h2>" + h(title(s)) + "</h2>",
        "<p>Status: REGISTERED_REFERENCE · " + h(s["source_title_status"]) + "</p>",
        '<p><a href="' + h(s["target_url"]) + '" rel="external noopener">' + h(s["target_url"]) + "</a></p>",
        d,
        "<p>Reference kind: " + h(s["reference_kind"]) + "</p>",
        "<p>Source title status: " + h(s["source_title_status"]) + "</p>",
        "<p>Source description status: " + h(s["source_description_status"]) + "</p>",
        "<p>Source publication date: " + h(date) + "</p>",
        "<p>Channel registration time: " + r["registration_time"]["utc"] + "; anchor " + str(r["registration_time"]["unix_epoch"]) + "</p>",
        "<p>Source observation scope: " + h(s["source_observation"]["scope"]) + "</p>",
        "<h2>Identity and evidence boundary</h2>",
        "<p>This page is an AIONARC_CHANNEL reference registration. Its URL is the channel permalink; the external target URL remains a separate source reference. Registration does not prove source claims or establish canonical status.</p>",
        "<p>Missing metadata remains OPEN. External source publication dates are distinct from channel registration time.</p>",
        "<footer>PROOF_BEFORE_STATE · UNKNOWN_BY_DEFAULT · DERIVED_IS_NOT_CANONICAL</footer>",
        "</body></html>"
    ]
    return "\n".join(lines) + "\n"

def homepage(r, ss):
    items = []
    for s in reversed(ss):
        items.append('<li><a href="' + h(s["channel_page"]) + '">' + h(s["signal_id"]) +
                     "</a> — " + h(title(s)) + ' — <a href="' + h(s["target_url"]) +
                     '">external source</a></li>')
    lines = [
        "<!doctype html>",
        '<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">',
        "<title>AIONARC_CHANNEL — Public Reference Register</title>",
        '<meta name="description" content="AIONARC_CHANNEL public reference register with 17 operator-bound destinations and machine-readable feeds.">',
        '<link rel="canonical" href="' + BASE + '">',
        '<link rel="alternate" type="application/rss+xml" href="' + BASE + 'rss.xml">',
        '<link rel="alternate" type="application/atom+xml" href="' + BASE + 'atom.xml">',
        '<link rel="alternate" type="application/feed+json" href="' + BASE + 'feed.json">',
        '<link rel="hub" href="' + HUB + '"></head><body>',
        "<h1>AIONARC_CHANNEL</h1>",
        "<p>Public reference and distribution channel for selected K501 Information Space sources. Not the canonical K501 Information Space.</p>",
        "<p>Active namespace: AIONARC_SIGNAL_NNNN · Assigned: 17 · Latest: AIONARC_SIGNAL_0017</p>",
        "<p>Next slot: AIONARC_SIGNAL_0018 — OPEN / UNASSIGNED / NOT PUBLISHED</p>",
        "<p>Registry anchor: " + str(r["registration_time"]["unix_epoch"]) + " · " + r["registration_time"]["utc"] + "</p>",
        "<p>Channel registration time is not source publication time. Missing metadata remains OPEN or UNKNOWN. The old SIGNAL_NNNN generation is historical and is not remapped.</p>",
        "<h2>Feeds</h2>",
        '<p><a href="' + BASE + 'rss.xml">RSS 2.0</a> · <a href="' + BASE + 'atom.xml">Atom 1.0</a> · <a href="' + BASE + 'feed.json">JSON Feed 1.1</a> · <a href="' + BASE + 'sitemap.xml">Sitemap</a> · <a href="' + BASE + 'robots.txt">robots.txt</a></p>',
        "<p>WebSub hub: " + HUB + "</p>",
        "<h2>Registered references</h2><ol>",
        "\n".join(items),
        "</ol>",
        "<footer>PUBLICATION_LAYER_NOT_CANONICAL · PROOF_BEFORE_STATE · UNKNOWN_BY_DEFAULT</footer>",
        "</body></html>"
    ]
    return "\n".join(lines) + "\n"

def make_feeds(r, ss):
    ordered = list(reversed(ss))
    reg = r["registration_time"]
    rss_items = []
    for s in ordered:
        rss_items.extend([
            "<item>", "<title>" + x(title(s)) + "</title>", "<link>" + x(s["channel_page"]) + "</link>",
            '<guid isPermaLink="true">' + x(s["channel_page"]) + "</guid>",
            "<description>" + x(summary(s, r)) + "</description>", "<pubDate>" + reg["rfc822"] + "</pubDate>",
            "<category>" + x(s["reference_kind"]) + "</category>",
            '<source url="' + h(s["target_url"]) + '">External source reference</source>', "</item>"
        ])
    rss = "\n".join([
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">', "<channel>",
        "<title>AIONARC_CHANNEL</title>", "<link>" + BASE + "</link>",
        "<description>Operator-bound reference register; registration does not validate source claims.</description>",
        "<language>en</language>", "<lastBuildDate>" + r["updated_at_rfc822"] + "</lastBuildDate>",
        '<atom:link href="' + BASE + 'rss.xml" rel="self" type="application/rss+xml"/>',
        '<atom:link href="' + HUB + '" rel="hub"/>', "\n".join(rss_items), "</channel>", "</rss>"
    ]) + "\n"

    atom_entries = []
    for s in ordered:
        atom_entries.extend([
            "<entry>", "<title>" + x(title(s)) + "</title>", "<id>" + x(s["channel_page"]) + "</id>",
            '<link href="' + h(s["channel_page"]) + '" rel="alternate"/>',
            '<link href="' + h(s["target_url"]) + '" rel="related"/>',
            "<updated>" + r["updated_at"] + "</updated>", "<published>" + reg["utc"] + "</published>",
            "<summary>" + x(summary(s, r)) + "</summary>",
            '<category term="' + h(s["reference_kind"]) + '"/>', "</entry>"
        ])
    atom = "\n".join([
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<feed xmlns="http://www.w3.org/2005/Atom">', "<title>AIONARC_CHANNEL</title>", "<id>" + BASE + "</id>",
        '<link href="' + BASE + '" rel="alternate"/>',
        '<link href="' + BASE + 'atom.xml" rel="self" type="application/atom+xml"/>',
        '<link href="' + HUB + '" rel="hub"/>', "<updated>" + r["updated_at"] + "</updated>",
        "<subtitle>Operator-bound reference register; registration does not validate source claims.</subtitle>",
        "<author><name>K501 Information Space</name></author>", "\n".join(atom_entries), "</feed>"
    ]) + "\n"

    items = []
    for s in ordered:
        items.append({
            "id": s["channel_page"], "url": s["channel_page"], "external_url": s["target_url"],
            "title": title(s), "content_text": summary(s, r), "date_published": reg["utc"],
            "date_modified": r["updated_at"], "_k501_signal_id": s["signal_id"],
            "_k501_reference_kind": s["reference_kind"], "_k501_title_status": s["source_title_status"],
            "_k501_description_status": s["source_description_status"],
            "_k501_source_publication_date": s.get("source_publication_date")
        })
    jf = {
        "version": "https://jsonfeed.org/version/1.1", "title": "AIONARC_CHANNEL",
        "home_page_url": BASE, "feed_url": BASE + "feed.json",
        "description": "Operator-bound reference register; registration does not validate source claims.",
        "language": "en", "authors": [{"name": "K501 Information Space"}],
        "hubs": [{"type": "WebSub", "url": HUB}], "items": items,
        "_k501_registry_anchor": reg["unix_epoch"], "_k501_registry_id": r["artifact_id"],
        "_k501_active_identifier_namespace": "AIONARC_SIGNAL_NNNN"
    }
    return rss, atom, json.dumps(jf, ensure_ascii=False, indent=2) + "\n"

def generate():
    r, ss, key = read_state()
    rss, atom, jf = make_feeds(r, ss)
    out = {
        "index.html": homepage(r, ss), "rss.xml": rss, "atom.xml": atom, "feed.json": jf,
        "robots.txt": "User-agent: *\nAllow: /\nSitemap: " + BASE + "sitemap.xml\n",
        key + ".txt": key + "\n"
    }
    locations = [BASE] + [s["channel_page"] for s in ss]
    sm = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
        "\n".join("<url><loc>" + x(u) + "</loc><lastmod>" + r["updated_at"][:10] + "</lastmod></url>" for u in locations),
        "</urlset>"
    ]
    out["sitemap.xml"] = "\n".join(sm) + "\n"
    for s in ss:
        out["signals/" + s["signal_id"] + "/index.html"] = detail(s, r)
    return out

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    drift = []
    for relative, content in generate().items():
        path = ROOT / relative
        if args.check:
            if not path.is_file() or path.read_text(encoding="utf-8") != content:
                drift.append(relative)
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8", newline="\n")
    if drift:
        raise SystemExit("Generated output drift: " + ", ".join(drift))
    print(("BUILD_CHECK_PASS" if args.check else "BUILD_WRITE_PASS"))

if __name__ == "__main__":
    main()
