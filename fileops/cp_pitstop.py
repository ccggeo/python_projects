

import subprocess

import csv

with open('/Users/cgeorge/Documents/Book2.csv') as csvfile:
    readCSV = csv.reader(csvfile, dialect=csv.excel_tab)
    row1 =[]
   
   
    for row in readCSV:
        r = row[0]
        row1.append(r)


print(row1)


MACS =row1

print(MACS)
'''
for m in MACS:
	print('Processing %s' % m)
        subprocess.Popen(["ssh", "admin@%s" %m, "mkdir Users/Admin/Desktop/Pitstop"], shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        subprocess.call([""], shell=True)
	#subprocess.call(["scp -r /Users/cgeorge/Desktop/scp/Enfocus_PP_17_update1.dmg admin@%s:/tmp" % m], shell=True)'''
