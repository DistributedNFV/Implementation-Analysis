#!usr/bin/python
from socket import *
import hashlib

 
host1 = '172.31.9.111' # '127.0.0.1' can also be used
port1 = 52000
host2 = '172.31.14.117'
port2 = 52001
host3 = '172.31.12.98'
port3 = 52002
sock1 = socket()
sock2 = socket()
sock3 = socket()
#Connecting to socket
sock1.connect((host1, port1)) #Connect takes tuple of host and port
sock2.connect((host2,port2))
sock3.connect((host3,port3))
while True:
    file1=raw_input('Enter File name :')
    text=open(file1,'r').read()

    hash_object=hashlib.md5(file1)
    m=hash_object.hexdigest()
    n=int(m,16)%3

 
#Infinite loop to keep client running

    if n==0:
            sock1.send(text)
            data1=sock1.recv(1024)
            print data1
            open('result','w').write(data1)
            
          
    elif n==1:
            sock2.send(text)
            data2=sock2.recv(1024)
            print data2
            open('result','w').write(data2)
           
                 
    elif n==2:
            sock3.send(text)
            data3=sock3.recv(1024)
            print data3
            open('result','w').write(data3)
            
    
   
 
sock.close()
