import yt_dlp
import os

ydl_opts = {
    'username': 'oauth2',
    'password': '',
    'quiet': False
}

print("Testing OAuth2 flow...")
try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.extract_info("https://www.youtube.com/watch?v=BaW_jenozKc", download=False)
except Exception as e:
    print(str(e))
