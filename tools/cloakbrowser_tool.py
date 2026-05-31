# cloakbrowser_tool.py
# OpenClaw / Claude Code 通用浏览器工具
# 用法: python cloakbrowser_tool.py <url> [--screenshot] [--humanize]

import sys
import json
from cloakbrowser import launch

async def main():
    url = sys.argv[1] if len(sys.argv) > 1 else None
    humanize = '--humanize' in sys.argv
    screenshot = '--screenshot' in sys.argv
    
    if not url:
        print(json.dumps({"error": "URL required"}))
        return
    
    browser = await launch(headless=True)
    page = await browser.new_page()
    
    if humanize:
        await page.humanize()
    
    await page.goto(url, wait_until='networkidle')
    title = await page.title()
    text = await page.inner_text('body')
    
    result = {
        "url": url,
        "title": title,
        "text": text[:5000],
        "length": len(text)
    }
    
    if screenshot:
        await page.screenshot(path='screenshot.png')
        result["screenshot"] = "screenshot.png"
    
    await browser.close()
    print(json.dumps(result, ensure_ascii=False))

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
