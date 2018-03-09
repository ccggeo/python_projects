

import subprocess

MACS = ["", ""]    

#subprocess.Popen(["ssh", "%s" % MACS, COMMAND], shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

for m in MACS:
	print('Processing %s' % m)
	subprocess.call(["mkdir /Users/admin/Desktop/scp"], shell=True)
	#subprocess.call(["scp -r /Users/cgeorge/Desktop/scp/Enfocus_PP_17_update1.dmg admin@%s:/tmp" % m], shell=True)
