import time
import webbrowser
import random
import os

Time = time.strftime("%H:%M")

#create txt file with youtube URL
def createYT():
    try:
        if os.path.isfile("/tmp/YT.txt") == False:
            flags = os.O_CREAT | os.O_EXCL | os.O_WRONLY
            filecreate = os.open("YT.txt", flags)
            with open("YT.txt", "wb") as f:
                f.write("https://youtu.be/BZg8BhBWyo8")
    except:
        return

def main():
    print( "What time do you want to wake up?")
    print ("Use this form.\nExample: 06:30")
    Alarm = raw_input("> ")
    #open file with YT link
    with open("YT.txt") as f:
        content = f.readlines()
    Time = time.strftime("%H:%M:%S")

    while Time != Alarm:
        Time = time.strftime("%H:%M:%S")
        print "The time is " + Time
        time.sleep(1)

        #If the Time variable is equal to the Alarm string, this code activates
        if Time == Alarm:

            print "Time to Wake up!"
            #from the variable content, a random link is chosen and then that link is stored in random_video variable
            random_video = random.choice(content)
            #Using the webbrowser library, it opens this youtube video link.
            #The videos are varius aphex twin songs
            webbrowser.open(random_video)

createYT()
main()




#When the Time does not equal the Alarm time string given above, print the time

