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
UA="AIONARC_CHANNEL/1.0 (+https://k501-information-space.github.io/AIONARC_CHANNEL/Gateway.md)"
ALLOW=("server","www-authenticate","via","cf-ray","x-request-id","x-cache","location","retry-after","content-type")
def request(url,method="GET",data=None,headers=None):
 h={"User-Agent":UA,"Accept":"*/*"};h.update(headers or {})
 try:
  with urlopen(Request(url,data=data,headers=h,method=method),timeout=25) as r:
   return r.status,("" if method=="HEAD" else r.read().decode("utf-8","replace")),dict(r.headers.items())
 except HTTPError as e:return e.code,("" if method=="HEAD" else e.read().decode("utf-8","replace")),dict(e.headers.items()) if e.headers else {}
 except (URLError,TimeoutError) as e:return 0,str(e),{}
def safe(h):
 d={str(k).lower():str(v) for k,v in h.items()};return {k:d[k] for k in ALLOW if k in d}
def changes():
 ep=os.environ.get("GITHUB_EVENT_PATH")
 if not ep or not Path(ep).is_file():return [BASE],True
 e=json.loads(Path(ep).read_text());before=e.get("before");after=os.environ.get("GITHUB_SHA") or e.get("after")
 if not before or not after or set(before)=={"0"}:return [BASE]+[BASE+"signals/AIONARC_SIGNAL_{:04d}/".format(i) for i in range(1,18)],True
 diff=subprocess.run(["git","diff","--name-status","--find-renames",before,after],cwd=ROOT,text=True,capture_output=True,check=True).stdout
 urls=set();changed=False
 for line in diff.splitlines():
  p=line.split("\t")
  if len(p)<2:continue
  paths=p[1:] if p[0].startswith(("R","C")) else [p[1]]
  for path in paths:
   if path=="index.html":urls.add(BASE)
   m=re.fullmatch(r"signals/(AIONARC_SIGNAL_[0-9]{4})/index\.html",path)
   if m:urls.add(BASE+"signals/"+m.group(1)+"/");changed=True
   if path in FEEDS:changed=True
 return sorted(urls),changed
def wait_pages(key,rid):
 tests=[(BASE,"AIONARC_SIGNAL_0017"),(BASE+"rss.xml","AIONARC_SIGNAL_0017"),(BASE+"atom.xml","AIONARC_SIGNAL_0017"),(BASE+"feed.json",rid),(BASE+"sitemap.xml","AIONARC_SIGNAL_0017"),(BASE+key+".txt",key)]
 for n in range(36):
  bad=[]
  for url,marker in tests:
   code,body,headers=request(url)
   if code!=200 or marker not in body:bad.append(url+" HTTP "+str(code))
  if not bad:print("PAGES_PUBLIC_GET_CHECK_PASS checks=6");return
  print("Pages wait {}/36: {}".format(n+1,"; ".join(bad)));time.sleep(10)
 raise RuntimeError("New Pages outputs and IndexNow key are not publicly reachable")
def heads():
 res={};errors=[]
 for feed in FEEDS:
  code,body,headers=request(BASE+feed,method="HEAD");res[feed]={"head_status":code,"headers":safe(headers)}
  print("Topic HEAD",feed,"HTTP",code,json.dumps(safe(headers),sort_keys=True))
  if code<200 or code>=300:errors.append(feed+" HEAD HTTP "+str(code))
 return res,errors
def indexnow(urls,key):
 if not urls:return "SKIPPED_NO_CHANGED_OWNED_HTML_URLS"
 payload={"host":"k501-information-space.github.io","key":key,"keyLocation":BASE+key+".txt","urlList":urls}
 code,body,headers=request("https://api.indexnow.org/indexnow","POST",json.dumps(payload).encode("utf-8"),{"Content-Type":"application/json; charset=utf-8"})
 print("IndexNow HTTP",code,"URL count",len(urls),"headers",json.dumps(safe(headers),sort_keys=True))
 if code==200:return "SUBMISSION_ACCEPTED_HTTP_200"
 if code==202:return "ACCEPTED_PENDING_KEY_VALIDATION_HTTP_202"
 raise RuntimeError("IndexNow response was not HTTP 200/202: "+str(code)+" "+body[:300])
def websub(changed,topic):
 result={};errors=[]
 for feed in FEEDS:
  if not changed:result[feed]={"status":"SKIPPED_FEED_UNCHANGED"};continue
  data=urlencode({"hub.mode":"publish","hub.url":BASE+feed}).encode("utf-8")
  code,body,headers=request(HUB,"POST",data,{"Content-Type":"application/x-www-form-urlencoded"})
  v={"status":code,"headers":safe(headers),"body_excerpt":body[:300],"topic_head_status":topic.get(feed,{}).get("head_status")}
  result[feed]=v
  print("Switchboard",feed,"HTTP",code,"topic_HEAD",v["topic_head_status"],"headers",json.dumps(v["headers"],sort_keys=True),"body",v["body_excerpt"])
  if code<200 or code>=300:errors.append(feed+" HTTP "+str(code))
 return result,errors
def main():
 r=json.loads((ROOT/"signals/registry.json").read_text());key=(ROOT/"signals/indexnow.key").read_text().strip()
 urls,changed=changes()
 if not urls and not changed:print("No owned pages or feed changed; skipped");return
 wait_pages(key,r["artifact_id"]);topic,head_errors=heads();ix=indexnow(urls,key);ws,ws_errors=websub(changed,topic)
 report=["AIONARC_CHANNEL post-deployment notification diagnostics","IndexNow: "+ix,"Changed owned HTML URLs: "+str(len(urls)),"WebSub topic HEAD: "+json.dumps(topic,sort_keys=True),"WebSub publisher responses: "+json.dumps(ws,sort_keys=True),"WebSub topic HEAD errors: "+json.dumps(head_errors),"WebSub publish errors: "+json.dumps(ws_errors),"IndexNow receipt is not indexing proof.","Switchboard acceptance is not subscriber-delivery proof.","External targets were excluded from IndexNow."]
 summary=os.environ.get("GITHUB_STEP_SUMMARY")
 if summary:Path(summary).write_text("\n".join(report)+"\n")
 print("POST_DEPLOYMENT_NOTIFICATION_DIAGNOSTICS_COMPLETE")
 if head_errors or ws_errors:raise RuntimeError("WebSub diagnostics completed with errors: "+json.dumps(head_errors+ws_errors))
if __name__=="__main__":main()
