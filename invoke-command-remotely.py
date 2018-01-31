#!/usr/bin/python
import subprocess
import sys

def invokecommand(TARGET, USER, COMMAND):

    x = USER + "@" + TARGET
        #command to run on host
    ssh = subprocess.Popen(["ssh", "%s" % x, COMMAND], shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    result = ssh.stdout.readlines()
    if result == []:
        error = ssh.stderr.readlines()
        print >>sys.stderr, "ERROR: %s" % error
    else:
        for x in result:
            print(x)
#        print result

USER =   raw_input(['USER'])
TARGET = raw_input(['Target'])
COMMAND =  raw_input(['Command'])

invokecommand(TARGET, USER, COMMAND) 
