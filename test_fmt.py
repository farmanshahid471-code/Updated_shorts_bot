import yt_dlp
import os

ydl_opts = {
    "extractor_args": {
        "youtube": {
            "player_client": ["android", "web"],
            "client": ["android", "web"]
        }
    },
    "http_headers": {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    },
    "quiet": False
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.extract_info("https://www.youtube.com/watch?v=L80TxTYyOKU", download=False)
