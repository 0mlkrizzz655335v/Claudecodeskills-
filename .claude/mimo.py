"""
MiMo Multimodal Chat - Image/Video/Audio understanding
Usage:
  python mimo.py "question about an image" image.png
  python mimo.py "text question"
  python mimo.py "describe this" image1.png image2.jpg
"""
import sys, json, base64, requests, os, mimetypes

API_KEY = "sk-c8senhdq2tpmouk6ncqisduhya6f8kl5dhvoi3mysr7jt6ip"
BASE = "https://api.xiaomimimo.com/v1"
MODEL = "mimo-v2.5"

def encode_file(path):
    mime, _ = mimetypes.guess_type(path)
    if not mime:
        ext = os.path.splitext(path)[1].lower()
        mime_map = {".png":"image/png", ".jpg":"image/jpeg", ".jpeg":"image/jpeg",
                    ".gif":"image/gif", ".webp":"image/webp", ".mp4":"video/mp4",
                    ".mp3":"audio/mpeg", ".wav":"audio/wav", ".ogg":"audio/ogg"}
        mime = mime_map.get(ext, "image/png")
    with open(path, "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
    return f"data:{mime};base64,{b64}"

args = sys.argv[1:]
if not args:
    print(__doc__)
    sys.exit(1)

# Separate text question from file paths
files = [a for a in args if os.path.isfile(a)]
text = " ".join([a for a in args if a not in files])

if not text:
    text = "Describe this in detail. What do you see?"

# Build content array
content = []
for f in files:
    data_uri = encode_file(f)
    content.append({"type": "image_url", "image_url": {"url": data_uri}})
content.append({"type": "text", "text": text})

print(f"MiMo analyzing: {len(files)} file(s)...", flush=True)

r = requests.post(f"{BASE}/chat/completions",
    headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"},
    json={"model": MODEL, "messages": [{"role": "user", "content": content}], "max_tokens": 2000},
    timeout=120)

r.raise_for_status()
data = r.json()
reply = data["choices"][0]["message"]["content"]
reasoning = data["choices"][0]["message"].get("reasoning_content", "")
tokens = data["usage"]["total_tokens"]

if reasoning:
    try:
    print(f'[thinking] {reasoning[:300]}...')
except:
    print('[thinking] (unicode skipped)')
    print("---")
print(reply.encode('utf-8', errors='replace').decode('utf-8', errors='replace'))
print(f"\n[tokens: {tokens}]")
