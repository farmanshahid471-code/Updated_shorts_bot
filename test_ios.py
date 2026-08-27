import yt_dlp

ydl_opts = {
    "extractor_args": {
        "youtube": {
            "player_client": ["ios", "android", "tv"]
        }
    },
    "quiet": False
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    try:
        info = ydl.extract_info("https://www.youtube.com/watch?v=L80TxTYyOKU", download=False)
        print("Success! formats:", len(info.get('formats', [])))
    except Exception as e:
        print("FAILED:", e)
