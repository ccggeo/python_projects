import subprocess


input = raw_input('URL:')

def get_audio(URL):


    subprocess.call("youtube-dl --extract-audio --audio-format mp3 %s" % URL, shell=True)

get_audio(input)



