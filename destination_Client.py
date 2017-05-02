#!/usr/bin/env python

#######################################################################
#Code by Abhirami Shankar
#######################################################################

#######################################################################
#Header declarations
#######################################################################
import os.path
import os
#######################################################################

#######################################################################
#Code begins here
#######################################################################
if os.path.isfile('broadcast_data'):
	#print ("file exists")
	f1 = open('broadcast_data','r')
	for line in f1:
		if 'DMAC' in line:
			mac = line.split()
	#print mac[1]
	if mac[1] == "ddd.ccc.bbb.aaa":
		f2 = open('reply.txt','w')
		f2.write("2")
		f2.write("\t")
		f2.write("ddd.ccc.bbb.aaa")
		f2.write("\n")
		f2.close()
		os.system("rm -rf broadcast_data")

elif os.path.isfile('send_data'):
	f2 = open('reply.txt','w')
        f2.write("2")
        f2.write("\t")
        f2.write("ddd.ccc.bbb.aaa")
        f2.write("\n")
        f2.close()
#########################################################################
#Code ends here
#########################################################################	
