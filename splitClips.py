from moviepy.editor import VideoFileClip
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from glob import *
from ffmpeg import *
from math import *
import os

def split(chunks):
    chunks = int(chunks)
    clips = glob('Videos/*.mp4')

    for clip in clips:
        clip = VideoFileClip(clip)
        duration = clip.duration
        parts = floor(duration / chunks)
        name, ext = os.path.splitext(clip.filename)
        try:
            os.mkdir(name)
        except:
            print("Directory Exists")
        if (duration <= chunks):
            ffmpeg_extract_subclip(clip.filename, 0, duration, targetname = name + "\Part_" + str(parts) + ext)
            clip.close()
            os.remove(clip.filename)
            continue

        for i in range(parts):
            margin = 10 if (i != 0) else 0
            ffmpeg_extract_subclip(clip.filename, (chunks*i) - margin, chunks*(i+1), targetname = name + "\Part_" + str(i) + ext)
            last = chunks*(i+1)
        ffmpeg_extract_subclip(clip.filename, last - margin, duration, targetname = name + "\Part_" + str(parts) + ext)
        clip.close()
        os.remove(clip.filename)