# file: inquiry.py
# auth: Albert Huang <albert@csail.mit.edu>
# desc: performs a simple device inquiry followed by a remote name request of
#       each discovered device
# $Id: inquiry.py 401 2006-05-05 19:07:48Z albert $
#

import bluetooth as blue
import os
import time
import sys
OWNER = sys.argv[1]
#OWNER = 'XT1033'
flag = False
locked = False
while True:
	print("performing inquiry...")
	nearby_devices = blue.discover_devices(lookup_names = True)
	#print("found %d devices" % len(nearby_devices))
	for addr, name in nearby_devices:
#   		print("  %s - %s" % (addr, name))
		if name == OWNER:
			print " owner found "
	   		print("  %s - %s" % (addr, name))
			flag = True
			break
	if flag == True:
		if locked == True:
			os.system('gnome-screensaver-command -d')
			locked = False
		flag = False
	#	break
	else :
		print "Owner Not found...Trying again"
		if locked == False:
			os.system('gnome-screensaver-command -l')
			locked = True

		
print "exiting app"
