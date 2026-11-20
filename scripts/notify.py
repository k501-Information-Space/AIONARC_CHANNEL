#!/usr/bin/env python3
import json,os,re,subprocess,time
from pathlib import Path
from urllib.error import HTTPError,URLError
from urllib.parse import urlencode
from urllib.request import Request,urlopen
ROOT=Path(__file__).resolve().parents[1]
BASE="https://k501-information-space.github.io/AIONARC_CHANNEL/"
HUB="https://switchboard.p3k.io/"
FEEDS=("rss.xml","atom.xml","feed.json")
def request(url,method="GET",data=None,headers=None):
    try:
        with urlopen(Request(url,data=data,headers=headers or {},method=method),timeout=20) as r:
            return r.status,r.read().decode("utf-8","replace")
    except HTTPError as e:
        return e.code,e.read().decode("utf-8","replace")
    except (URLError,TimeoutError) as e:
        return 0,str(e)
def changes():
    ep=os.environ.get("GITHUB_EVENT_PATH")
    if not ep or not Path(ep).is_file():
        return [BASE],True
    event=json.loads(Path(ep).read_text(encoding="utf-8"))
    before=event.get("before")
    after=os.environ.get("GITHUB_SHA") or event.get("after")
    if not before or not after or set(before)=={"0"}:
        return [BASE]+[BASE+"signals/AIONARC_SIGNAL_{:04d}/".format(i) for i in range(1,18)],True
    diff=subprocess.run(["git","diff","--name-status","--find-renames",before,after],cwd=ROOT,text=True,capture_output=True,check=True).stdout
    urls=set()
    feed_changed=False
    for line in diff.splitlines():
        p=line.split("\t")
        if len(p)<2: continue
        paths=p[1:] if p[0].startswith(("R","C")) else [p[1]]
        for path in paths:
            if path=="index.html": urls.add(BASE)
            m=re.fullmatch(r"signals/(AIONARC_SIGNAL_[0-9]{4})/index\.html",path)
            if m:
                urls.add(BASE+"signals/"+m.group(1)+"/")
                feed_changed=True
            if path in FEEDS: feed_changed=True
    return sorted(urls),feed_changed
def wait_pages(key,registry_id):
    tests=[(BASE,"AIONARC_SIGNAL_0017"),(BASE+"rss.xml","AIONARC_SIGNAL_0017"),(BASE+"atom.xml","AIONARC_SIGNAL_0017"),(BASE+"feed.json",registry_id),(BASE+"sitemap.xml","AIONARC_SIGNAL_0017"),(BASE+key+".txt",key)]
    for n in range(36):
        failed=[]
        for url,marker in tests:
            status,body=request(url)
            if status!=200 or marker not in body: failed.append(url+" HTTP "+str(status))
        if not failed: return
        print("Pages wait {}/36: {}".format(n+1,"; ".join(failed)))
        time.sleep(10)
    raise RuntimeError("New Pages outputs and IndexNow key are not publicly reachable")
def send_indexnow(urls,key):
    if not urls: return "SKIPPED_NO_CHANGED_OWNED_HTML_URLS"
    payload={"host":"k501-information-space.github.io","key":key,"keyLocation":BASE+key+".txt","urlList":urls}
    for n in range(3):
        status,body=request("https://api.indexnow.org/indexnow","POST",json.dumps(payload).encode(),{"Content-Type":"application/json; charset=utf-8"})
        print("IndexNow HTTP",status,"URL count",len(urls))
        if status==200: return "SUBMISSION_ACCEPTED_HTTP_200"
        if status==202: return "ACCEPTED_PENDING_KEY_VALIDATION_HTTP_202"
        if status not in (0,429): raise RuntimeError("IndexNow rejected request: "+str(status)+" "+body[:300])
        time.sleep(30*(n+1))
    raise RuntimeError("IndexNow did not return HTTP 200/202")
def publish_websub(feed_changed):
    result={}
    for feed in FEEDS:
        if not feed_changed:
            result[feed]="SKIPPED_FEED_UNCHANGED"
            continue
        data=urlencode({"hub.mode":"publish","hub.url":BASE+feed}).encode()
        status,body=request(HUB,"POST",data,{"Content-Type":"application/x-www-form-urlencoded"})
        print("Switchboard",feed,"HTTP",status)
        if status<200 or status>=300: raise RuntimeError("Switchboard rejected "+feed+": "+str(status)+" "+body[:300])
        result[feed]="PUBLISH_REQUEST_ACCEPTED_HTTP_"+str(status)
    return result
def main():
    r=json.loads((ROOT/"signals/registry.json").read_text(encoding="utf-8"))
    key=(ROOT/"signals/indexnow.key").read_text(encoding="utf-8").strip()
    urls,feeds_changed=changes()
    if not urls and not feeds_changed:
        print("No owned pages or feed changed; skipped")
        return
    wait_pages(key,r["artifact_id"])
    ix=send_indexnow(urls,key)
    ws=publish_websub(feeds_changed)
    report=["AIONARC_CHANNEL notification result","IndexNow: "+ix,"Changed owned HTML URLs: "+str(len(urls)),"Switchboard: "+json.dumps(ws,sort_keys=True),"IndexNow receipt is not indexing proof.","Switchboard acceptance is not subscriber-delivery proof.","External targets were excluded from IndexNow."]
    summary=os.environ.get("GITHUB_STEP_SUMMARY")
    if summary: Path(summary).write_text("\n".join(report)+"\n",encoding="utf-8")
    print("POST_DEPLOYMENT_NOTIFICATIONS_COMPLETE")
if __name__=="__main__": main()
