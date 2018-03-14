

import subprocess
import csv
import socket

with open('.csv', 'rU') as csvfile:
    readCSV = csv.reader(csvfile, dialect=csv.excel_tab)
    row1 =[]
   
   
    for row in readCSV:
        r = row[0]
        row1.append(r)

MACS = row1

print(MACS)
for m in MACS:
	#print('Processing %s' % m)

	TARGET = m
	def is_connected():
	  try:
	    host = socket.gethostbyname(TARGET)
	    s = socket.create_connection((host, 22), 2)
	    return 1
	  except:
	     pass
	  return 0
	CONNECTED = is_connected()
	if CONNECTED == 1:
		x = "<localadmin>" + "@" + m
		COMMAND = "ssh-copy-id" + " " + x 
		result = subprocess.call([COMMAND], shell=True)
		print(result)
	
	else:
		print("the ting goes")
