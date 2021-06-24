import glob
import os
import subprocess

for f in glob.glob("*.wav"):
    f2 = f[0:-3] + "mp3"
    if not os.path.exists(f2):
        subprocess.call(["ffmpeg", "-i", f, f2])
