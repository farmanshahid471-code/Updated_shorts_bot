from pathlib import Path
cookie_path = Path("/root/Updated_shorts_bot/yt_shorts_bot/cookies.txt")
if cookie_path.exists():
    text = cookie_path.read_text(errors="replace")
    if "# Netscape HTTP Cookie File" not in text:
        print("FAIL: Not a Netscape cookie file.")
    elif ".youtube.com" not in text:
        print("FAIL: No YouTube cookies found.")
    else:
        auth = any(x in text for x in ["SID", "APISID", "HSID", "SSID", "SAPISID", "__Secure-1PSID"])
        print(f"SUCCESS: File exists and looks like a YouTube cookie file. Contains Auth Markers: {auth}")
else:
    print("FAIL: File does not exist.")
