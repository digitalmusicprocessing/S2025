import glob
import subprocess

files = glob.glob("*.wav")
files = sorted(files)
s = ""
for f in files:
    p = f.split(".wav")[0]
    fout = "{}.m4a".format(p)
    subprocess.call(["ffmpeg", "-i", f, fout])