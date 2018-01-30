#!/usr/bin/python



def invoke-command:

    import subprocess
    import sys



    HOST=""
    USER=raw_input(['USERNAME OF USER'])
    #command to run on host

    COMMAND=""

    ssh = subprocess.Popen(["ssh", "%s" % HOST, COMMAND], shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    result = ssh.stdout.readlines()
    if result == []:
        error = ssh.stderr.readlines()
        print >>sys.stderr, "ERROR: %s" % error
    else:
        print result


invoke-command() 
