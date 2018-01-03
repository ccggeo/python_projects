#!/usr/bin/python

import subprocess
import sys

HOST="user@FQDN"

#command to run on host

COMMAND="w"

ssh = subprocess.Popen(["ssh", "%s" % HOST, COMMAND], shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

result = ssh.stdout.readlines()
if result == []:
    error = ssh.stderr.readlines()
    print >>sys.stderr, "ERROR: %s" % error
else:
    print result
    
