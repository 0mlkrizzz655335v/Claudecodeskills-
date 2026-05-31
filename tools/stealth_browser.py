#!/usr/bin/env python3
"""stealth_browser.py v2 — 七层反反爬融合工具"""

import sys, json, asyncio, random

def fetch_curl_cffi(url):
    """L5: TLS指纹伪装 Chrome/Firefox/Safari"""
    try:
        from curl_cffi import requests
        browsers = ["chrome124","chrome120","chrome110","firefox120","safari17_0"]
        r = requests.get(url, impersonate=random.choice(browsers), timeout=15)
        return {"engine":"curl-cffi","status":r.status_code,"text":r.text[:8000],"len":len(r.text)}
    except Exception as e:
        return {"engine":"curl-cffi","error":str(e)}

def fetch_fake_ua(url):
    """L6: 随机UA轮换+httpx"""
    try:
        from fake_useragent import UserAgent; import httpx
        ua = UserAgent()
        h = {"User-Agent":ua.random,"Accept":"text/html,application/xhtml+xml","Accept-Language":"en-US,en;q=0.5","DNT":"1"}
        r = httpx.get(url, headers=h, timeout=15, follow_redirects=True)
        return {"engine":"fake-ua+httpx","status":r.status_code,"ua":h["User-Agent"][:60],"text":r.text[:8000],"len":len(r.text)}
    except Exception as e:
        return {"engine":"fake-ua+httpx","error":str(e)}

async def fetch_nodriver(url):
    try:
        import nodriver as uc
        b = await uc.start(headless=True); p = await b.get(url)
        t = p.title; c = await p.get_content(); b.stop()
        return {"engine":"nodriver","title":str(t),"text":str(c)[:8000],"len":len(str(c))}
    except Exception as e:
        return {"engine":"nodriver","error":str(e)}

async def fetch_nodriver_fp(url):
    try:
        import nodriver as uc; from browserforge.headers import HeaderGenerator
        h = HeaderGenerator().generate()
        b = await uc.start(headless=True,browser_args=[f"--user-agent={h['User-Agent']}"])
        p = await b.get(url); t = p.title; c = await p.get_content(); b.stop()
        return {"engine":"nodriver+browserforge","title":str(t),"text":str(c)[:8000],"len":len(str(c))}
    except Exception as e:
        return {"engine":"nodriver+browserforge","error":str(e)}

async def fetch_rebrowser(url):
    try:
        from playwright.async_api import async_playwright
        async with async_playwright() as pw:
            b = await pw.chromium.launch(headless=True,args=["--disable-blink-features=AutomationControlled","--no-sandbox"])
            ctx = await b.new_context(viewport={"width":1920,"height":1080})
            p = await ctx.new_page()
            await p.add_init_script("Object.defineProperty(navigator,'webdriver',{get:()=>undefined});window.chrome={runtime:{}};")
            await p.goto(url,wait_until="domcontentloaded",timeout=30000)
            t = await p.title(); c = await p.inner_text("body"); await b.close()
            return {"engine":"rebrowser","title":t,"text":c[:8000],"len":len(c)}
    except Exception as e:
        return {"engine":"rebrowser","error":str(e)}

async def fetch_cloakbrowser(url):
    try:
        from cloakbrowser import launch
        b = await launch(headless=True); p = await b.new_page()
        await p.goto(url,wait_until="domcontentloaded")
        t = await p.title(); c = await p.inner_text("body"); await b.close()
        return {"engine":"cloakbrowser","title":t,"text":c[:8000],"len":len(c)}
    except Exception as e:
        return {"engine":"cloakbrowser","error":str(e)}

ENGINES = {
    1:("nodriver",fetch_nodriver,False),2:("nodriver+browserforge",fetch_nodriver_fp,False),
    3:("rebrowser",fetch_rebrowser,False),4:("cloakbrowser",fetch_cloakbrowser,False),
    5:("curl-cffi(TLS)",fetch_curl_cffi,True),6:("fake-ua+httpx",fetch_fake_ua,True),
}

async def smart_fetch(url,level=1):
    n,f,s = ENGINES.get(min(level,6),ENGINES[1])
    return f(url) if s else await f(url)

async def fallback_fetch(url):
    for lvl in [5,6,1,2,3,4]:
        try:
            n,f,s = ENGINES[lvl]; r = f(url) if s else await f(url)
            if r and "error" not in r: r["fallback_lvl"]=lvl; return r
        except: continue
        await asyncio.sleep(0.3)
    return {"error":"all 6 layers failed"}

async def main():
    import argparse
    p = argparse.ArgumentParser(); p.add_argument("url",nargs="?")
    p.add_argument("--level",type=int,default=1); p.add_argument("--fallback",action="store_true"); p.add_argument("--list",action="store_true")
    a = p.parse_args()
    if a.list:
        for k,v in ENGINES.items(): print(f"  L{k} {v[0]}")
        return
    if not a.url: print(json.dumps({"error":"URL required"},ensure_ascii=False)); return
    r = await fallback_fetch(a.url) if a.fallback else await smart_fetch(a.url,a.level)
    print(json.dumps(r,ensure_ascii=False,indent=2))

if __name__=="__main__": asyncio.run(main())