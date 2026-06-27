"""
Image generation via Volcano Engine Seedream 4.5
Usage: python gen_img.py "prompt" [output_path]
"""
import sys, json, base64, requests, os

API_KEY = "49436fc3-872b-41e8-82dc-dacf2929ccf2"
ENDPOINT = "ep-20260529232711-bmq4r"
BASE = "https://ark.cn-beijing.volces.com/api/v3"

if len(sys.argv) < 2:
    print(__doc__)
    sys.exit(1)

prompt = sys.argv[1]
output = sys.argv[2] if len(sys.argv) > 2 else "generated.png"

headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

r = requests.post(f"{BASE}/images/generations",
    headers=headers,
    json={
        "model": ENDPOINT,
        "prompt": prompt,
        "size": "1024x1024",
        "n": 1,
        "response_format": "b64_json"
    },
    timeout=120)

data = r.json()
if r.status_code != 200:
    print(f"ERROR: {json.dumps(data, ensure_ascii=False)[:500]}")
    sys.exit(1)

img = data["data"][0]
if "b64_json" in img:
    with open(output, "wb") as f:
        f.write(base64.b64decode(img["b64_json"]))
elif "url" in img:
    import urllib.request
    urllib.request.urlretrieve(img["url"], output)
else:
    print(f"ERROR: no image data. keys={list(img.keys())}")
    sys.exit(1)

size_kb = os.path.getsize(output) / 1024
print(f"OK {output} ({size_kb:.0f}KB) | prompt: {prompt[:60]}...")
