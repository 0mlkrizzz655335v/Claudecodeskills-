"""
Video generation via Volcano Engine Seedance 1.5 Pro
Usage: python gen_vid.py "prompt" [output_path]
"""
import sys, json, requests, os, time

API_KEY = "49436fc3-872b-41e8-82dc-dacf2929ccf2"
ENDPOINT = "ep-20260529233146-dgp7c"
BASE = "https://ark.cn-beijing.volces.com/api/v3"

if len(sys.argv) < 2:
    print(__doc__)
    sys.exit(1)

prompt = sys.argv[1]
output = sys.argv[2] if len(sys.argv) > 2 else "generated.mp4"

headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

print(f"Submitting: {prompt[:80]}...")
r = requests.post(f"{BASE}/contents/generations/tasks",
    headers=headers,
    json={"model": ENDPOINT, "content": [{"type": "text", "text": prompt}]},
    timeout=30)

r.raise_for_status()
task_id = r.json()["id"]
print(f"Task: {task_id}")

for i in range(120):
    time.sleep(5)
    r2 = requests.get(f"{BASE}/contents/generations/tasks/{task_id}",
        headers=headers, timeout=15)
    status = r2.json()
    state = status.get("status", "unknown")
    print(f"  [{i+1}] {state}")

    if state == "succeeded":
        # Find video_url anywhere in response
        def find_url(obj):
            if isinstance(obj, str) and obj.startswith("http"):
                return obj
            if isinstance(obj, dict):
                for k, v in obj.items():
                    if k == "video_url" and isinstance(v, str):
                        return v
                    r = find_url(v)
                    if r: return r
            if isinstance(obj, list):
                for item in obj:
                    r = find_url(item)
                    if r: return r
            return None

        url = find_url(status)
        if url:
            import urllib.request
            urllib.request.urlretrieve(url, output)
            size_mb = os.path.getsize(output) / 1024 / 1024
            print(f"SUCCESS! {output} ({size_mb:.1f} MB)")
            print(f"  Resolution: {status.get('resolution','?')} | Duration: {status.get('duration','?')}s | FPS: {status.get('framespersecond','?')}")
        else:
            print(f"ERROR: no URL found")
        sys.exit(0)

    elif state == "failed":
        print(f"ERROR: {json.dumps(status, ensure_ascii=False)[:500]}")
        sys.exit(1)

print("TIMEOUT")
sys.exit(1)
