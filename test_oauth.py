import yt_dlp
ydl_opts = {
    "username": "oauth2",
    "password": "",
    "quiet": False
}
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    pass
