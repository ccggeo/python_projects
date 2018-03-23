#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import datetime
import webbrowser
import random
import os

Time = time.strftime("%H:%M")
#Validate timeinput
def timevalidate(Alarm):
    try:
        Time = datetime.datetime.strptime(Alarm, "%H:%M")
    except ValueError:
        raise ValueError("Incorrect Time Format or invalid time. Must be in HH:M")
        return False
#Create YT URL text file

def createYT():
    try:
        if os.path.isfile("/tmp/YT.txt") == False:
            flags = os.O_CREAT | os.O_EXCL | os.O_WRONLY
            filecreate = os.open("/tmp/YT.txt", flags)
            with open("/tmp/YT.txt", "wb") as f:
                f.write("https://youtu.be/BZg8BhBWyo8")
    except:
        return
#main function
def main():
    print( "What time do you want to wake up?")
    print ("Use this form.\nExample: 06:30")
    Alarm = raw_input("> ")
    timevalidate(Alarm)

    with open("/tmp/YT.txt") as f:
        content = f.readlines()
    Time = time.strftime("%H:%M")

    if Alarm == Time:
        print "Alarm cannot be set to current time"
        exit()
    else:

        while Time != Alarm:
            Time = time.strftime("%H:%M")
            seconds = time.strftime("%H:%M:%S")
            print "The time is " + seconds
            time.sleep(1)

            if Time == Alarm:
                print "Time to Wake up!"
                random_video = random.choice(content)
                webbrowser.open(random_video)

createYT()
main()


