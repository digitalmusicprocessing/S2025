import subprocess
import glob

for f in glob.glob("*.wav"):
    subprocess.call(["ffmpeg", "-i", f, f[0:-3] + "mp3"])
