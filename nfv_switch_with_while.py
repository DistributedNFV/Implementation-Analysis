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
#variable declarations
#######################################################################
MAC_entries = []
#source_mac =[]
#######################################################################

#######################################################################
#Code starts here
#######################################################################
while(True):
	f = open( 'header.txt', 'a+' )

	for line in f:
        	line = line.strip()
        	if 'SMAC' in line:
                	source_mac = [str(line.split()[1])]
        	if 'DMAC' in line:
                	dest_mac = [str(line.split()[1])]

	if os.path.isfile('CAM_table'):
        	if os.path.isfile('reply.txt'):
                	f5 = open('CAM_table','a+')
                	for line in f5:
                        	MAC_entries = [str(line.split()[1])]
                	print(MAC_entries)
                	if dest_mac[0] not in MAC_entries:
                        	f6 = open('reply.txt','r')
                        	for line in f6:
                                	f5.write(line)
                                	line = line.split()[1]
                               		MAC_entries.append(str(line))
                        	f5.close()
                        	f6.close()
                		print(MAC_entries)
                	os.system("rm -rf reply.txt")
       		else:
                	pass
	else:
        	f1 = open( 'CAM_table', 'w' )
         	f1.write("1")
         	f1.write('\t')
         	f1.write(source_mac[0])
         	f1.write("\n")
         	f1.close()

         	dmac_search = open( 'CAM_table', 'r' )

         	for line in dmac_search:
                	line = line.strip()
                	macs = line.split()[1]
                	if not MAC_entries:
                        	print('creating MAC entries')
                        	MAC_entries = [macs]

	
        if str(dest_mac[0]) not in MAC_entries:
                print('dest mac not found')
                f2 = open ('header.txt', 'a+')

		f3 = open('broadcast_data', 'a+' )
                for line in f2:
                         f3.write(line)
                f3.close()
                f2.close()

        elif str(dest_mac[0]) in MAC_entries:
                if os.path.isfile('send_data'):
                        print('DMAC present')
                        pass
                else:
                        print('DMAC present')
                        f8 = open('send_data','a+')
                        f9 = open('header.txt','a+')
                        for line in f9:
                                f8.write(line)
                        f8.write('\n')
                        f8.write('hello how are you')
                        f8.write('\n')
                        f8.close()

#############################################################################
#Code ends here
#############################################################################
