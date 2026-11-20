#!/usr/bin/env python3
"""Build the active AIONARC_CHANNEL public projection from signals/registry.json."""
import argparse, html, json, re
from pathlib import Path
from xml.sax.saxutils import escape
ROOT=Path(__file__).resolve().parents[1]
BASE="https://k501-information-space.github.io/AIONARC_CHANNEL/"
HUB="https://switchboard.p3k.io/"
def h(v): return html.escape(str(v if v is not None else ""),quote=True)
def x(v): return escape(str(v if v is not None else ""))
def main():
    p=argparse.ArgumentParser()
    p.add_argument("--check",action="store_true")
    a=p.parse_args()
    r=json.loads((ROOT/"signals/registry.json").read_text(encoding="utf-8"))
    ss=r["signals"]
    key=(ROOT/"signals/indexnow.key").read_text(encoding="utf-8").strip()
    if len(ss)!=17 or not re.fullmatch(r"[A-Za-z0-9-]{8,128}",key):
        raise SystemExit("Registry or IndexNow key invalid")
    def title(s): return s.get("verified_source_title") or s["signal_id"]+" — Source title not supplied or observed"
    def desc(s): return s.get("verified_source_description") or "Source description OPEN; only the operator-supplied target URL is registered."
    def summary(s): return desc(s)+" External target: "+s["target_url"]+". Channel registration: "+r["registration_time"]["utc"]+"."
    outputs={}
    home=["<!doctype html>",'<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1>',"<title>AIONARC_CHANNEL</title>",'<link rel="canonical" href="'+BASE+'">','<link rel="alternate" type="application/rss+xml" href="'+BASE+'rss.xml">','<link rel="alternate" type="application/atom+xml" href="'+BASE+'atom.xml">','<link rel="alternate" type="application/feed+json" href="'+BASE+'feed.json">','<link rel="hub" href="'+HUB+'"></head><body>',"<h1>AIONARC_CHANNEL</h1>","<p>Public reference and distribution channel; not the canonical K501 Information Space.</p>","<p>Assigned references: 17 · Latest: AIONARC_SIGNAL_0017</p>","<p>AIONARC_SIGNAL_0018 remains OPEN / UNASSIGNED / NOT PUBLISHED.</p>","<h2>Registered references</h2><ol>"]
    rss=["<?xml version='1.0' encoding='UTF-8'?>","<rss version='2.0' xmlns:atom='http://www.w3.org/2005/Atom'><channel>","<title>AIONARC_CHANNEL</title>","<link>"+BASE+"</link>","<atom:link href='"+BASE+"rss.xml' rel='self' type='application/rss+xml'/>","<atom:link href='"+HUB+"' rel='hub'/>"]
    atom=["<?xml version='1.0' encoding='UTF-8'?>","<feed xmlns='http://www.w3.org/2005/Atom'><title>AIONARC_CHANNEL</title>","<id>"+BASE+"</id>","<link href='"+BASE+"atom.xml' rel='self'/>","<link href='"+HUB+"' rel='hub'/>","<updated>"+r["updated_at"]+"</updated>"]
    items=[]
    for s in reversed(ss):
        page=["<!doctype html>",'<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1>','<title>'+h(s["signal_id"])+" — "+h(title(s))+"</title>",'<link rel="canonical" href="'+h(s["channel_page"])+'">','<link rel="hub" href="'+HUB+'"></head><body>',"<h1>"+h(s["signal_id"])+"</h1>","<h2>"+h(title(s))+"</h2>",'<p><a href="'+h(s["target_url"])+'">'+h(s["target_url"])+"</a></p>","<p>"+h(desc(s))+"</p>","<p>Channel registration: "+r["registration_time"]["utc"]+"</p>","<p>Registration does not prove source claims or canonical status.</p>","</body></html>"]
        outputs["signals/"+s["signal_id"]+"/index.html"]="\n".join(page)+"\n"
        home.append('<li><a href="'+h(s["channel_page"])+'">'+h(s["signal_id"])+"</a> — "+h(title(s))+"</li>")
        summ=x(summary(s))
        rss.append("<item><title>"+x(title(s))+"</title><link>"+x(s["channel_page"])+"</link><guid>"+x(s["channel_page"])+"</guid><description>"+summ+"</description></item>")
        atom.append("<entry><title>"+x(title(s))+"</title><id>"+x(s["channel_page"])+"</id><link href='"+h(s["channel_page"])+"' rel='alternate'/><updated>"+r["updated_at"]+"</updated><summary>"+summ+"</summary></entry>")
        items.append({"id":s["channel_page"],"url":s["channel_page"],"external_url":s["target_url"],"title":title(s),"content_text":summary(s),"_k501_signal_id":s["signal_id"]})
    home.extend(["</ol>","<p><a href='rss.xml'>RSS 2.0</a> · <a href='atom.xml'>Atom 1.0</a> · <a href='feed.json'>JSON Feed 1.1</a></p>","</body></html>"])
    outputs["index.html"]="\n".join(home)+"\n"
    rss.extend(["</channel>","</rss>"])
    outputs["rss.xml"]="\n".join(rss)+"\n"
    atom.extend(["</feed>"])
    outputs["atom.xml"]="\n".join(atom)+"\n"
    outputs["feed.json"]=json.dumps({"version":"https://jsonfeed.org/version/1.1","title":"AIONARC_CHANNEL","home_page_url":BASE,"feed_url":BASE+"feed.json","hubs":[{"type":"WebSub","url":HUB}],"items":items},ensure_ascii=False,indent=2)+"\n"
    outputs["robots.txt"]="User-agent: *\nAllow: /\nSitemap: "+BASE+"sitemap.xml\n"
    outputs[key+".txt"]=key+"\n"
    locs=[BASE]+[s["channel_page"] for s in ss]
    outputs["sitemap.xml"]="\n".join(["<?xml version='1.0' encoding='UTF-8'?>","<urlset xmlns='http://www.sitemaps.org/schemas/sitemap/0.9'>","\n".join("<url><loc>"+x(u)+"</loc></url>" for u in locs),"</urlset"])+"\n"
    if a.check:
        missing=[p for p in outputs if not (ROOT/p).is_file()]
        if missing: raise SystemExit("Missing generated outputs: "+", ".join(missing))
        print("BUILD_CHECK_PASS outputs_present="+str(len(outputs)))
    else:
        for path,content in outputs.items():
            target=ROOT/path
            target.parent.mkdir(parents=True,exist_ok=True)
            target.write_text(content,encoding="utf-8",newline="\n")
        print("BUILD_WRITE_PASS outputs="+str(len(outputs)))
if __name__=="__main__":
    main()
