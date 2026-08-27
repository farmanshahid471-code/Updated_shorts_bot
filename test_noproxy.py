import yt_dlp

ydl_opts = {
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
