"""
multimedia.py - Image/Video/Audio processing toolkit
Usage: python multimedia.py <action> <args...>

Actions:
  img_resize   <input> <output> <width> <height>        Resize image
  img_convert  <input> <output>                         Convert image format  
  img_compress <input> <output> <quality(1-100)>        Compress image
  vid_trim     <input> <output> <start> <duration>      Trim video
  vid_convert  <input> <output>                         Convert video format
  vid_extract_audio <input> <output>                    Extract audio from video
  aud_trim     <input> <output> <start> <duration>      Trim audio
  aud_convert  <input> <output>                         Convert audio format
  img_screenshot <output>                               Take screenshot
"""

import sys, subprocess
from PIL import Image
import os

def img_resize(inp, out, w, h):
    img = Image.open(inp)
    img = img.resize((int(w), int(h)), Image.LANCZOS)
    img.save(out)
    print(f"OK: {out} ({img.size[0]}x{img.size[1]})")

def img_convert(inp, out):
    Image.open(inp).save(out)
    print(f"OK: {out}")

def img_compress(inp, out, quality=85):
    img = Image.open(inp)
    if img.mode in ("RGBA", "P"):
        img = img.convert("RGB")
    img.save(out, quality=int(quality), optimize=True)
    orig = os.path.getsize(inp)
    new = os.path.getsize(out)
    print(f"OK: {out} ({new/1024:.0f}KB, was {orig/1024:.0f}KB)")

def img_screenshot(out):
    from PIL import ImageGrab
    img = ImageGrab.grab()
    img.save(out)
    print(f"OK: {out} ({img.size[0]}x{img.size[1]})")

def run_ffmpeg(args, desc):
    cmd = ["ffmpeg", "-y", "-hide_banner", "-loglevel", "error"] + args
    subprocess.run(cmd, check=True)
    print(f"OK: {desc}")

def vid_trim(inp, out, start, dur):
    run_ffmpeg(["-ss", start, "-i", inp, "-t", dur, "-c", "copy", out], out)

def vid_convert(inp, out):
    run_ffmpeg(["-i", inp, "-c:v", "libx264", "-preset", "fast", "-crf", "23", out], out)

def vid_extract_audio(inp, out):
    run_ffmpeg(["-i", inp, "-vn", "-acodec", "libmp3lame", "-q:a", "2", out], out)

def aud_trim(inp, out, start, dur):
    run_ffmpeg(["-ss", start, "-i", inp, "-t", dur, "-c", "copy", out], out)

def aud_convert(inp, out):
    run_ffmpeg(["-i", inp, out], out)

if __name__ == "__main__":
    actions = {
        "img_resize": img_resize, "img_convert": img_convert,
        "img_compress": img_compress, "img_screenshot": img_screenshot,
        "vid_trim": vid_trim, "vid_convert": vid_convert,
        "vid_extract_audio": vid_extract_audio,
        "aud_trim": aud_trim, "aud_convert": aud_convert,
    }
    if len(sys.argv) < 2 or sys.argv[1] not in actions:
        print(__doc__)
        sys.exit(1)
    fn = actions[sys.argv[1]]
    args = sys.argv[2:]
    try:
        fn(*args)
    except Exception as e:
        print(f"ERROR: {e}")
        sys.exit(1)
