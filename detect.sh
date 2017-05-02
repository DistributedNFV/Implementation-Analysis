#!/bin/bash

while [ 1 ]
do
        inotifywait $HOME/Project/MenuSelection.txt > /dev/null && echo -e "Instruction received.\n"
        sleep 0.15
        INSTRUCTION=$(cat $HOME/Project/MenuSelection.txt)
        echo -e "Acting as ${INSTRUCTION}\n"
	if [[ $INSTRUCTION = 'NAT' ]] || [[ $INSTRUCTION = 'Firewall' ]]
	then
		echo -e "${INSTRUCTION} function exists on edge.\n"
	else
		echo -e "${INSTRUCTION} function does not exist on edge. Choosing best cloud server for retreival.\n"
		./choose_cloud_server.py
		IP=$(cat $HOME/Project/ChosenIp.txt)
		rm -rf ChosenIp.txt
		echo ""
	fi
	if [ $INSTRUCTION = 'Switch' ]
	then
		echo -e "Network Function: Switch\n"
		scp -r ec2-user@$IP:switch/* .
		./nfv_switch_with_while.py
	fi
	if [ $INSTRUCTION = 'Firewall' ]
	then
		echo -e "Network Function: Firewall\n"
		python test.py
	fi
done

