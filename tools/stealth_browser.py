#!/usr/bin/env python3
"""
stealth_browser.py — 多层反检测浏览器融合工具
整合: CloakBrowser(C++) + nodriver(CDP) + browserforge(指纹) + rebrowser(JS补丁)
用法: python stealth_browser.py <url> [--level 1-4] [--screenshot] [--text]

安全层:
  L1 nodriver     — 纯Python CDP直连, 最快, 日常用
  L2 browserforge — 智能指纹轮换, 搭配L1/L3
  L3 rebrowser    — JS级Playwright补丁, 按需开关
  L4 CloakBrowser — C++源码修补, 极端反爬场景
"""

import sys
import json
import asyncio
import random
import time
from pathlib import Path

LEVELS = {
    1: "nodriver",
    2: "nodriver + browserforge",
    3: "rebrowser + browserforge",
    4: "cloakbrowser"
}

async def fetch_nodriver(url, humanize=False):
    """L1: 纯Python CDP, 最快"""
    try:
        import nodriver as uc
        browser = await uc.start(headless=True)
        page = await browser.get(url)
        title = page.title
        text = await page.get_content()
        browser.stop()
        return {"engine": "nodriver", "title": str(title), "text": str(text)[:8000], "len": len(str(text))}
    except Exception as e:
        return {"engine": "nodriver", "error": str(e)}

async def fetch_nodriver_fingerprint(url):
    """L2: nodriver + 随机指纹"""
    try:
        import nodriver as uc
        from browserforge.headers import HeaderGenerator
        from browserforge.fingerprints import FingerprintGenerator

        headers = HeaderGenerator().generate()
        fingerprint = FingerprintGenerator().generate()

        browser = await uc.start(
            headless=True,
            browser_args=[
                f"--user-agent={headers['User-Agent']}",
                f"--accept-language={headers.get('Accept-Language', 'en-US,en;q=0.9')}"
            ]
        )
        page = await browser.get(url)
        title = page.title
        text = await page.get_content()
        browser.stop()
        return {
            "engine": "nodriver+browserforge",
            "title": title,
            "text": text[:8000],
            "len": len(text),
            "fingerprint": fingerprint.navigator.userAgent[:40]
        }
    except Exception as e:
        return {"engine": "nodriver+browserforge", "error": str(e)}

async def fetch_rebrowser(url):
    """L3: Playwright + rebrowser JS补丁"""
    try:
        from playwright.async_api import async_playwright
        
        async with async_playwright() as p:
            browser = await p.chromium.launch(
                headless=True,
                args=[
                    "--disable-blink-features=AutomationControlled",
                    "--no-sandbox"
                ]
            )
            context = await browser.new_context(
                viewport={"width": 1920, "height": 1080},
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36"
            )
            page = await context.new_page()
            
            # 注入反检测脚本
            await page.add_init_script("""
                Object.defineProperty(navigator, 'webdriver', {get: () => undefined});
                Object.defineProperty(navigator, 'plugins', {get: () => [1,2,3,4,5]});
                Object.defineProperty(navigator, 'languages', {get: () => ['en-US', 'en']});
                window.chrome = {runtime: {}};
            """)
            
            await page.goto(url, wait_until="domcontentloaded", timeout=30000)
            title = await page.title()
            text = await page.inner_text("body")
            await browser.close()
            return {"engine": "rebrowser+playwright", "title": title, "text": text[:8000], "len": len(text)}
    except Exception as e:
        return {"engine": "rebrowser+playwright", "error": str(e)}

async def fetch_cloakbrowser(url):
    """L4: C++级隐身, 极端场景"""
    try:
        from cloakbrowser import launch
        browser = await launch(headless=True)
        page = await browser.new_page()
        await page.goto(url, wait_until="domcontentloaded")
        title = await page.title()
        text = await page.inner_text("body")
        await browser.close()
        return {"engine": "cloakbrowser", "title": title, "text": text[:8000], "len": len(text)}
    except Exception as e:
        return {"engine": "cloakbrowser", "error": str(e)}

async def fetch_with_fallback(url, level=1):
    """带降级的智能抓取: L1失败 → L2 → L3 → L4"""
    engines = []
    
    if level >= 1:
        engines.append(("L1-nodriver", fetch_nodriver))
    if level >= 2:
        engines.append(("L2-fingerprint", fetch_nodriver_fingerprint))
    if level >= 3:
        engines.append(("L3-rebrowser", fetch_rebrowser))
    if level >= 4:
        engines.append(("L4-cloakbrowser", fetch_cloakbrowser))
    
    for name, func in engines:
        try:
            result = await func(url)
            if "error" not in result:
                result["fallback_level"] = name
                return result
        except Exception:
            continue
        await asyncio.sleep(0.5)
    
    return {"error": "所有引擎均失败", "tried": [e[0] for e in engines]}

async def main():
    import argparse
    parser = argparse.ArgumentParser(description="多层反检测浏览器")
    parser.add_argument("url", nargs="?", help="目标URL")
    parser.add_argument("--level", type=int, default=1, choices=[1,2,3,4], help="反检测级别 (1-4)")
    parser.add_argument("--fallback", action="store_true", help="自动降级 (L1失败→L4)")
    parser.add_argument("--text", action="store_true", help="只返回文本")
    parser.add_argument("--list", action="store_true", help="列出所有引擎")
    
    args = parser.parse_args()
    
    if args.list:
        print(json.dumps(LEVELS, ensure_ascii=False, indent=2))
        return
    
    if not args.url:
        print(json.dumps({"error": "URL required", "levels": LEVELS}, ensure_ascii=False))
        return
    
    if args.fallback:
        result = await fetch_with_fallback(args.url, 4)
    else:
        mapping = {1: fetch_nodriver, 2: fetch_nodriver_fingerprint, 
                   3: fetch_rebrowser, 4: fetch_cloakbrowser}
        func = mapping[args.level]
        result = await func(args.url)
    
    if args.text and "text" in result:
        print(result["text"])
    else:
        print(json.dumps(result, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    asyncio.run(main())
