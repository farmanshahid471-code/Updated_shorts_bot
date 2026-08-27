import yt_dlp
import os

proxy = "http://jgrwxmfm:1523zxrdn5ll@31.59.20.176:6754"

ydl_opts = {
    "proxy": proxy,
    "extractor_args": {
        "youtube": {
            "player_client": ["ios", "android", "tv"]
        }
    },
    "quiet": False
}

try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.extract_info("https://www.youtube.com/watch?v=L80TxTYyOKU", download=False)
    print("SUCCESS")
except Exception as e:
    print(f"FAILED: {e}")
