# Implementation-Analysis
Implementation and Analysis of Distributed Network Functions Virtualization

# Authors
Abhirami Shankar, Aditya Saroja Hariharakrishnan, Omkar Dattatraya Pawar, Hariram Natarajan, Shriya Rodi, and Antara Kolar

# Abstract
A majority of communication service providers are using Network Function Virtualization (NFV) currently as a method to accelerate service delivery and reduce associated overhead and costs at the same time. Ease of deployment, vendor independence and cost reduction are some of the factors that NFV addresses. While distributed systems have for long been used to provide decentralized operation, through this paper we propose a system to integrate NFV and distributed systems, so that the advantages of either system can be enhanced upon with the other. We focus mainly on the customer edge and the distributed cloud. Evaluations for the system are primarily on the latency and round trip time measured by comparing with a centralized system where all the functions are present in the cloud verses functions being distributed over the entire architecture.

# Available files
1. EdgeAddress               - Stores the IP address of the Edge device
2. Firewall.py               - Runs the firewall NFV
3. IPPacket.pkt              - IP Packet format
4. Menu.sh                   - User Interface for clients
5. NAT.py                    - Runs the NAT NFV
6. RoutingTable.tab          - Routing Table of the Router
7. choose_cloud_server.py    - Chooses the best cloud server
8. destination_Client.py     - Destination client simulator for switch
9. detect.sh                 - Main shell script running on edge
10. header.txt               - Switch frame
11. input.txt                - Input for Firewall NFV
12. load.py                  - Load Balancer NFV
13. nat_input                - Input to NAT Function
14. nat_table                - NAT Rules
15. nfv_switch_with_while.py - Main Switch NFV
16. private_to_public.txt    - NAT output
17. public_to_private.txt    - NAT input
18. remover.sh               - Cleaner script
19. result                   - Load Balancer output
20. router.py                - Main Router NFV
21. rules.txt                - Firewall rules
22. server1.py               - Load balancer Server code
23. server_database.txt      - List of distributed cloud servers
