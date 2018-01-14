import subprocess

URL = "https://www.youtube.com/watch?v=sB6HY8r983c"

subprocess.call("youtube-dl --extract-audio --audio-format mp3 %s" % URL, shell=True)
