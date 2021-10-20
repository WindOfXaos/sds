from glob import *
import youtube_dl
import os

def down():
    ydl_opts = {
        'format':'(mp4)[height<=360]',
        'outtmpl': '/Videos/%(title)s.%(ext)s'
    }
    file = glob('./*.list')

    for line in open(file[0]).read().splitlines():
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([line])

    os.remove(file[0])
