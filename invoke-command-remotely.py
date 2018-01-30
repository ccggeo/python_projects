#!/usr/bin/python
import subprocess
import sys

def invokecommand(TARGET, USER, COMMAND):

    x = USER + "@" + TARGET
        #command to run on host
    #https://stackoverflow.com/questions/7468668/python-subprocess-readlines
    ssh = subprocess.Popen(["ssh", "%s" % x, COMMAND], shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    result = ssh.stdout.readlines()
    if result == []:
        error = ssh.stderr.readlines()
        print >>sys.stderr, "ERROR: %s" % error
    else:
        print result

USER =  raw_input(['USERNAME OF USER'])
TARGET = raw_input(['USERNAME OF Target'])
COMMAND =  raw_input(['USERNAME OF Command'])

invokecommand(TARGET, USER, COMMAND) 
