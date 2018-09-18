# coding=utf-8
import urllib2
import os
import platform
import uuid
import sys
from json import load
from urllib2 import urlopen

# startup stuff
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=25, cols=100))
from colorama import Fore, Back, Style
print Fore.BLUE
# startup stuff end ------

# Start Clear
cls = lambda: os.system('clear')
cls()
# end Clear ------

# Hand Wave Start
hand = """
_      ___ _______
|  _,-' _ `\______)
|~'    ' `\()
|       (____)
|      (_____)
|--.____(___)
"""
# Hand End ---------

# logo
logo = """
  █    ██  ███▄    █   ██████  ▒█████   █    ██  ██▀███   ▄████▄  ▓█████ ▓█████▄ 
  ██  ▓██▒ ██ ▀█   █ ▒██    ▒ ▒██▒  ██▒ ██  ▓██▒▓██ ▒ ██▒▒██▀ ▀█  ▓█   ▀ ▒██▀ ██▌
 ▓██  ▒██░▓██  ▀█ ██▒░ ▓██▄   ▒██░  ██▒▓██  ▒██░▓██ ░▄█ ▒▒▓█    ▄ ▒███   ░██   █▌
 ▓▓█  ░██░▓██▒  ▐▌██▒  ▒   ██▒▒██   ██░▓▓█  ░██░▒██▀▀█▄  ▒▓▓▄ ▄██▒▒▓█  ▄ ░▓█▄   ▌
 ▒▒█████▓ ▒██░   ▓██░▒██████▒▒░ ████▓▒░▒▒█████▓ ░██▓ ▒██▒▒ ▓███▀ ░░▒████▒░▒████▓ 
 ░▒▓▒ ▒ ▒ ░ ▒░   ▒ ▒ ▒ ▒▓▒ ▒ ░░ ▒░▒░▒░ ░▒▓▒ ▒ ▒ ░ ▒▓ ░▒▓░░ ░▒ ▒  ░░░ ▒░ ░ ▒▒▓  ▒ 
 ░░▒░ ░ ░ ░ ░░   ░ ▒░░ ░▒  ░ ░  ░ ▒ ▒░ ░░▒░ ░ ░   ░▒ ░ ▒░  ░  ▒    ░ ░  ░ ░ ▒  ▒ 
  ░░░ ░ ░    ░   ░ ░ ░  ░  ░  ░ ░ ░ ▒   ░░░ ░ ░   ░░   ░ ░           ░    ░ ░  ░ 
    ░              ░       ░      ░ ░     ░        ░     ░ ░         ░  ░   ░    
                                                        ░                ░                                                                                                                   
"""
print logo
# end logo ----

# Pc Info

ps = platform.processor()
sy = platform.system()
op = platform.platform()
vs = platform.version()
ma = platform.machine()

Operating_System_Processor = "\n Your Operating System Processor : " + ps
Operating_System_Uname = "\n Your Operating System : " + sy
Operating_System = "\n Your Operating System Full : " + op
Operating_System_Version = "\n Your Operating System Version : " + vs
Operating_System_Machine = "\n Your Operating System Machine : " + ma

Show_Operating_Info = Operating_System + Operating_System_Version + Operating_System_Machine + Operating_System_Uname + Operating_System_Processor
# pc info end ----

# ip get start
IP = "http://ip.42.pl/raw"
IPRead = urllib2.urlopen(IP)
ReadIP = IPRead.read()
IP_2 = load(urlopen('http://jsonip.com'))['ip']
IpInfo = " Your IP : " + ReadIP + "\n Your Ip (2) : " + IP_2


# ip get end ------

# get Mac Address Start
def get_mac():
    mac_num = hex(uuid.getnode()).replace('0x', '').upper()
    mac = '-'.join(mac_num[i: i + 2] for i in range(0, 11, 2))
    return mac


Mac = get_mac()
MacInfo = "\n Your Mac Address Is : " + Mac
# get Mac Address end -----

# print info Function
PInfo = IpInfo + MacInfo
# end print info Function -----

# Print Information in console
print PInfo
print Show_Operating_Info

System_Info_Txt = open("Info.txt", "w")
System_Info_Txt.write(PInfo + Show_Operating_Info)
System_Info_Txt.close()

try:
    input(Fore.GREEN + "\n\n\n [ Press Enter To Continue ]")
except SyntaxError:
    pass

cls()

print Fore.YELLOW + hand + "\n Bye Bye"
# End --------------
