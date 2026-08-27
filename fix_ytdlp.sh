#!/bin/bash
echo "Testing yt-dlp version..."
/root/Updated_shorts_bot/.venv/bin/python -c "import yt_dlp; print(yt_dlp.version.__version__)"
