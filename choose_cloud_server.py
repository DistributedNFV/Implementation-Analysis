#!/usr/bin/env python

#########################################################################
# Code by Abhirami Shankar
#########################################################################

#########################################################################
#Headers
#########################################################################
import subprocess
import os
import operator
from collections import OrderedDict 
#import file
import math
#import file

#########################################################################
#variable declarations
#########################################################################
IP_addr = []
rtt = {}
min_val = 1000.0


#Code begins here########################################################
f1 = open('server_database.txt','r')

for line in f1:
	line = line.strip()
	IP = line.split()[0]
	if not IP_addr:
		IP_addr = [IP]
	else:
		IP_addr.append(IP)	

#print(IP_addr)
for i in range(0,len(IP_addr)):
	string = 'ping -s 32 -c 5\t' + IP_addr[i] +'\t | tail -2'
	print 'Trying to connect to server with IP: \t'+ IP_addr[i]
	#print '\n'
	var = subprocess.check_output(string, shell=True)
	var = var.strip()
	var5 = var.split('\n')
	var8 = var5[0].split(',')
	packet_loss = var8[2].split()[0]
	if str(packet_loss) == '100%':
		pass
	else:
		var1 = var5[1].split('=')[1]
		var2 = var1.split('/')[1]
		var2 = var2.strip("'")
		var2 = float(var2)
		#print('Time taken to connect to server'+ IP_addr[i] + str(var2) )
		if IP_addr[i] not in rtt:
			rtt[IP_addr[i]] = float(var2)
print "\n"
#print rtt
for item in rtt:
	print('Time taken to connect to '+item+' is '+str(rtt[item]))
	if float(rtt[item]) < float(min_val):
		min_val = rtt[item]
		closest_IP = item
		
f10 = open('ChosenIp.txt','w')
f10.write(closest_IP)
f10.close()
#print(closest_IP)

#code Ends here###############################################################
