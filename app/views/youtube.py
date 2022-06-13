from __future__ import unicode_literals
from yt_dlp import YoutubeDL

import os
import glob

def youtube_download(url):
    # os.remove("")
    files = glob.glob('uploads/youtube*', recursive=True)

    for f in files:
        try:
            os.remove(f)
        except OSError as e:
            print("Error: %s : %s" % (f, e.strerror))

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '192'
        }],
        'postprocessor_args': [
            '-ar', '16000',
            '-ac', '1'
        ],
        'outtmpl': 'uploads/youtube.%(ext)s',
        # 'prefer_ffmpeg': True,
        'keepvideo': True
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    return 'uploads/youtube.wav'

if __name__ == "__main__":
    youtube_download("https://www.youtube.com/watch?v=inpDLQLqSik")
