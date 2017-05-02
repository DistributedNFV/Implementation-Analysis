#!/bin/bash

RETRY=1
ATTEMPTS=3
ADDRESS=$(cat $HOME/Project/EdgeAddress)

echo -e "Hello SysAdmin! Please select your functionality\n\n1. Router\n2. Switch\n3. NAT\n4. Firewall\n5. Load Balancer\n"

while [ $RETRY = 1 ] && [ $ATTEMPTS != 0 ]
do
	read userInput

	if [ "$userInput" = "Router" ]
	then
		echo $userInput > $HOME/Project/MenuSelection.txt
		RETRY=0
	elif [ "$userInput" = "Switch" ]
	then
		echo $userInput > $HOME/Project/MenuSelection.txt
		RETRY=0
	elif [ "$userInput" = "Switch" ]
	then
		echo $userInput > $HOME/Project/MenuSelection.txt
		RETRY=0
	elif [ "$userInput" = "NAT" ]
	then
		echo $userInput > $HOME/Project/MenuSelection.txt
		RETRY=0
	elif [ "$userInput" = "Firewall" ]
	then
		echo $userInput > $HOME/Project/MenuSelection.txt
		RETRY=0
	elif [ "$userInput" = "Load Balancer" ]
	then
		echo $userInput > $HOME/Project/MenuSelection.txt
		RETRY=0
	else
		ATTEMPTS=$((ATTEMPTS-1))
		echo -e "Incorrect option. ${ATTEMPTS} attempt(s) left.\n"
	fi
done

if [ $ATTEMPTS = 0 ]
then
	echo -e "Exiting.\n"
else
	ping -c 1 $ADDRESS > /dev/null
	if [ $? == 0 ]
	then
		scp $HOME/Project/MenuSelection.txt ec2-user@$ADDRESS:/home/ec2-user/Project/MenuSelection.txt > /dev/null
		echo -e "Choice sent to edge gateway.\n"	
	else
		echo -e "Edge gateway unreachable.\n"
	fi	
fi
