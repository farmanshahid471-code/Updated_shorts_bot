import urllib.request
import json
try:
    req = urllib.request.Request("https://raw.githubusercontent.com/yt-dlp/yt-dlp/master/yt_dlp/extractor/youtube.py")
    with urllib.request.urlopen(req) as response:
        content = response.read().decode('utf-8')
        if 'po_token' in content.lower():
            print("PO Token support is available in yt-dlp source")
        else:
            print("No PO token support found")
except Exception as e:
    print(str(e))
