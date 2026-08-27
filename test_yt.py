import yt_dlp
ydl_opts = {
    "cookiefile": "yt_shorts_bot/cookies.txt",
    "quiet": False
}
try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.extract_info("https://www.youtube.com/watch?v=PBTDmlB47zc", download=False)
except Exception as e:
    print(str(e))
