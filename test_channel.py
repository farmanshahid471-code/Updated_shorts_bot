import yt_dlp

ydl_opts = {
    "extract_flat": True,
    "playlist_items": "1-5",
    "extractor_args": {
        "youtube": {
            "player_client": ["ios", "android"],
            "player_skip": ["webpage"]
        }
    },
    "quiet": False
}

try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info("https://www.youtube.com/@IShowSpeed/streams", download=False)
        print("Success! Videos:", len(info.get('entries', [])))
except Exception as e:
    print("FAILED:", e)
