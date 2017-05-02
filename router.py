# This device has two interfaces, int1 and int2
# Network on int1: 1.0.0.0/30
# Network on int2: 2.0.0.0/30
# MAC address of edge (this device): aaa.aaa.aaa.aaa
# MAC address of next hop: bbb.bbb.bbb.bbb

import os

_data = "/home/adsa2112/Project/IPPacket.pkt"									# Path to input packet.
_table = "/home/adsa2112/Project/RoutingTable.tab"								# Path to routing table.

if (not os.path.isfile (_data)):												# If input packet does not exist, quit.
	print ("Packet not available.\n")
else:
	inputPacket = open (_data, "r")
	routingTable = open (_table, "a+")

	if (not os.path.isfile (_table)):											# If routing table does not exist, create.
		routingTable.write ("1.0.0.0/30 is directly connected, int1\n" +
			"1.0.0.1/32 is directly connected, int1\n" +
			"2.0.0.0/30 is directly connected, int2\n" +
			"2.0.0.1/32 is directly connected, int2")

	packetLines = inputPacket.readlines ()
	sourceIP = packetLines[0].split (": ")[1].rstrip ()
	sourceMAC = packetLines[1].split (": ")[1].rstrip ()
	destMAC = packetLines[2].split (": ")[1].rstrip ()
	destIP = packetLines[3].split (": ")[1].rstrip ()

	if int (sourceIP.split("/")[1]) != 32 or int (destIP.split("/")[1]) != 32:
		print ("Our router function cannot handle non /32 networks for now.\n")

	rtngTblLines = routingTable.readlines ()
	rtngTbIP = []
	for i in range (0, len (rtngTblLines)):
		rtngTbIP.append (rtngTblLines[i].split ()[0])
	if sourceIP in rtngTbIP:
		print ("Source IP in routing table.\n")
	else:
		routingTable.write ("\n" + format (sourceIP) + " via 1.0.0.1, int1")
	if destIP in rtngTbIP:
		print ("Destination IP in routing table.\n")
	else:
		# Perform ARP here.
		routingTable.write ("\n" + format (destIP) + " via 2.0.0.1, int2")