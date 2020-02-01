#!/usr/bin/env python
# encoding: utf-8
"""
autoinstall.py

Created by N16HT_W4RR10R on 01/02/2020.
Copyright (c) 2020 Copyright Holder. All rights reserved.
"""
import time, sys, threading, os, urllib, json, subprocess, socket, select, platform
from os import system
from platform import python_version
pv = python_version()
if sys.version[0] in '2':
	system('clear')
	exit("\r\033[32;1m[\033[31;1m!\033[32;1m]\033[33;1m gunakan python versi 3 tong..!!\x1b[0m\n")

g = "\033[32;1m"
gt = "\033[0;32m"
bt = "\033[34;1m"
b = "\033[36;1m"
m = "\033[31;1m"
c = "\033[0m"
p = "\033[37;1m"
u = "\033[35;1m"
M = "\033[3;1m"
k = "\033[33;1m"
kt = "\033[0;33m"
a = "\033[30;1m"

W = '\x1b[0m'
R = '\x1b[31m'
G = '\x1b[1;32m'
O = '\x1b[33m'
B = '\x1b[34m'
P = '\x1b[35m'
C = '\x1b[36m'
GR = '\x1b[37m'


def slowaprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(7.0 / 90)

def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(2.0 / 90)
      
def tanya():
	    print("\n")
	    dicobalagi = input(k+"Kembali Ke Menu Utama? [y/t] "+m+": "+p)
	    if dicobalagi.lower() == "y":
        	main_menu()
	    elif dicobalagi.lower() == "t":
        	system('clear')
        	sys.exit(m+"Dadah :)\n"+W)
	    else :
        	print(k+"Pilihannya Cuma y dan t Doang tong -_- ")
	        tanya()
      
def clear():
    return os.system("cls") if (platform.system() == 'Windows') else os.system("clear")
      
def main_menu():
       clear()
       slowprint(W + '#'*46)
       slowprint(W + '|         -== '+bt+'Tools Auto Install'+W+' ==-         |')
       slowprint(W + '| Author'+m+'  :'+g+' '+M+'N16HT_W4RR10R'+W+'                    |')
       slowprint(W + '| Github  '+m+':'+M+' '+p+'https://github.com/N16HT-W4RR10R'+W+' |')
       slowprint(W + '| Contact '+m+':'+M+' '+u+'https://t.me/N16HT_W4RR10R'+W+'       |')
       slowprint(W + '#'*46)
       print(W + '# ' + str(time.strftime('%a, %d %B %Y')))
       print(W + '# Provider gsm Operator ' + C + str(os.popen('getprop gsm.operator.alpha').read().split('\n')[0]))
       print(W + '# Python ' + C + str(pv) + W + ', ' + C + str(os.popen('getprop ro.product.device').read().split('\n')[0]) + ' ' + str(os.popen('getprop ro.build.version.release').read().split('\n')[0]) + ' Build SDK ' + str(os.popen('getprop ro.build.version.sdk').read().split('\n')[0]))
       print(W + '#'*46)
       
       
       slowaprint (gt+"Menu Pilihan:")
       print (gt+"  ["+p+"1"+gt+"] "+p+"Install Admin Finder")
       print (gt+"  ["+p+"2"+gt+"] "+p+"Install airack-ng")
       print (gt+"  ["+p+"3"+gt+"] "+p+"Install Admin Panel Finder")
       print (gt+"  ["+p+"4"+gt+"] "+p+"Install Arch Linux")
       print (gt+"  ["+p+"5"+gt+"] "+p+"Install Auxscan2.0")
       print (gt+"  ["+p+"5"+gt+"] "+p+"Install A-Rat")
       print (gt+"  ["+p+"6"+gt+"] "+p+"Install AstraNmap")
       print (gt+"  ["+p+"7"+gt+"] "+p+"Install Bluepot")
       print (gt+"  ["+p+"8"+gt+"] "+p+"Install BinGoo")
       print (gt+"  ["+p+"9"+gt+"] "+p+"Install BlueMaho")
       print (gt+"  ["+p+"10"+gt+"] "+p+"Install BruteSploit")
       print (gt+"  ["+p+"11"+gt+"] "+p+"Install Bing Dorker")
       print (gt+"  ["+p+"12"+gt+"] "+p+"Install Bing-Ip2hosts")
       print (gt+"  ["+p+"13"+gt+"] "+p+"Install BruteXSS")
       print (gt+"  ["+p+"14"+gt+"] "+p+"Install BlackMail")
       print (gt+"  ["+p+"15"+gt+"] "+p+"Install Blacktrack")
       print (gt+"  ["+p+"16"+gt+"] "+p+"Install Bughunter")
       print (gt+"  ["+p+"17"+gt+"] "+p+"Install BlackNmap")
       print (gt+"  ["+p+"18"+gt+"] "+p+"Install Black-Hydra")
       print (gt+"  ["+p+"19"+gt+"] "+p+"Install Cok-Rat")
       print (gt+"  ["+p+"20"+gt+"] "+p+"Install Cupp")
       print (gt+"  ["+p+"21"+gt+"] "+p+"Install Clone E-mail")
       print (gt+"  ["+p+"22"+gt+"] "+p+"Install CMSmap")
       print (gt+"  ["+p+"23"+gt+"] "+p+"Install Com Foxcontact Exploiter")
       print (gt+"  ["+p+"24"+gt+"] "+p+"Install Com_Fabrik Exploiter")
       print (gt+"  ["+p+"25"+gt+"] "+p+"Install CMS Scanner")
       print (gt+"  ["+p+"26"+gt+"] "+p+"Install ComLap")
       print (gt+"  ["+p+"27"+gt+"] "+p+"Install Compiler Python")
       print (gt+"  ["+p+"28"+gt+"] "+p+"Install Comz")
       print (gt+"  ["+p+"29"+gt+"] "+p+"Install DeShal")
       slowprint (gt+"  ["+p+"30"+gt+"] "+p+"Install Dark-fb")
       print (gt+"  ["+p+"31"+gt+"] "+p+"Install Dirbuster")
       print (gt+"  ["+p+"32"+gt+"] "+p+"Install D-Tect")
       print (gt+"  ["+p+"33"+gt+"] "+p+"Install Decodify")
       print (gt+"  ["+p+"34"+gt+"] "+p+"Install DDOS")
       print (gt+"  ["+p+"35"+gt+"] "+p+"Install Dracnmap")
       print (gt+"  ["+p+"36"+gt+"] "+p+"Install Dec-Enc-Hash")
       print (gt+"  ["+p+"37"+gt+"] "+p+"Install Datasploit")
       print (gt+"  ["+p+"38"+gt+"] "+p+"Install Email-Harvester")
       print (gt+"  ["+p+"39"+gt+"] "+p+"Install Ezsploit")
       print (gt+"  ["+p+"40"+gt+"] "+p+"Install Encrypt-Python")
       print (gt+"  ["+p+"41"+gt+"] "+p+"Install Find-Shell")
       print (gt+"  ["+p+"42"+gt+"] "+p+"Install FlipTracker")
       print (gt+"  ["+p+"43"+gt+"] "+p+"Install Gps-Tracking")
       print (gt+"  ["+p+"44"+gt+"] "+p+"Install Google-Dork")
       print (gt+"  ["+p+"45"+gt+"] "+p+"Install Hash-Buster")
       print (gt+"  ["+p+"46"+gt+"] "+p+"Install HashTool")
       print (gt+"  ["+p+"47"+gt+"] "+p+"Install Hunner")
       print (gt+"  ["+p+"48"+gt+"] "+p+"Install HostChecker")
       print (gt+"  ["+p+"49"+gt+"] "+p+"Install Hash Code")
       slowaprint (gt+"  ["+p+"50"+gt+"] "+p+"Install Information Gathering")
       print (gt+"  ["+p+"51"+gt+"] "+p+"Install IPGeolocation")
       print (gt+"  ["+p+"52"+gt+"] "+p+"Install Ipddos")
       print (gt+"  ["+p+"53"+gt+"] "+p+"Install IP-Tracer")
       print (gt+"  ["+p+"54"+gt+"] "+p+"Install Joomscan")
       print (gt+"  ["+p+"55"+gt+"] "+p+"Install Kali Nethunter")
       print (gt+"  ["+p+"56"+gt+"] "+p+"Install Ko-Dork")
       print (gt+"  ["+p+"57"+gt+"] "+p+"Install Lazymux")
       print (gt+"  ["+p+"58"+gt+"] "+p+"Install Lazysqlmap")
       print (gt+"  ["+p+"59"+gt+"] "+p+"Install Lokomedia Exploiter")
       print (gt+"  ["+p+"60"+gt+"] "+p+"Install Linux Fedora")
       print (gt+"  ["+p+"61"+gt+"] "+p+"Install LITESPAM")
       print (gt+"  ["+p+"62"+gt+"] "+p+"Install Mail-Spammer")
       print (gt+"  ["+p+"63"+gt+"] "+p+"Install MyServer")
       print (gt+"  ["+p+"64"+gt+"] "+p+"Install Microsploit")
       print (gt+"  ["+p+"65"+gt+"] "+p+"Install Md5-Crack")
       print (gt+"  ["+p+"66"+gt+"] "+p+"Install NMapForAndroid")
       print (gt+"  ["+p+"67"+gt+"] "+p+"Install OWASP-Nettacker")
       print (gt+"  ["+p+"68"+gt+"] "+p+"Install PenBox")
       print (gt+"  ["+p+"69"+gt+"] "+p+"Install Port-Lookup")
       slowprint (gt+"  ["+p+"70"+gt+"] "+p+"Install Reposcanner")
       print (gt+"  ["+p+"71"+gt+"] "+p+"Install RouterSploit")
       print (gt+"  ["+p+"72"+gt+"] "+p+"Install Red Hawk")
       print (gt+"  ["+p+"73"+gt+"] "+p+"Install SFile")
       print (gt+"  ["+p+"74"+gt+"] "+p+"Install S-Mbf")
       print (gt+"  ["+p+"75"+gt+"] "+p+"Install Saycheese")
       print (gt+"  ["+p+"76"+gt+"] "+p+"Install SQLMap")
       print (gt+"  ["+p+"77"+gt+"] "+p+"Install Scanner Tools")
       print (gt+"  ["+p+"78"+gt+"] "+p+"Install Sarahah-XSS-Exploit")
       print (gt+"  ["+p+"79"+gt+"] "+p+"Install Sqli-Scanner")
       print (gt+"  ["+p+"80"+gt+"] "+p+"Install Sqliv")
       print (gt+"  ["+p+"81"+gt+"] "+p+"Install Server_Domains")
       print (gt+"  ["+p+"82"+gt+"] "+p+"Install Torshammer")
       print (gt+"  ["+p+"83"+gt+"] "+p+"Install Thanatos")
       print (gt+"  ["+p+"84"+gt+"] "+p+"Install TrackUrl")
       print (gt+"  ["+p+"85"+gt+"] "+p+"Install The Fat Rat")
       print (gt+"  ["+p+"86"+gt+"] "+p+"Install Ubuntu")
       print (gt+"  ["+p+"87"+gt+"] "+p+"Install Universal Fedora Chroot Tool")
       print (gt+"  ["+p+"88"+gt+"] "+p+"Install ViSQL")
       print (gt+"  ["+p+"89"+gt+"] "+p+"Install VulnScaner")
       print (gt+"  ["+p+"90"+gt+"] "+p+"Install WPScan")
       print (gt+"  ["+p+"91"+gt+"] "+p+"Install Wordpress Brute Force")
       print (gt+"  ["+p+"92"+gt+"] "+p+"Install Wordpress Security Scanner")
       print (gt+"  ["+p+"93"+gt+"] "+p+"Install Weeman")
       print (gt+"  ["+p+"94"+gt+"] "+p+"Install Webdav")
       print (gt+"  ["+p+"95"+gt+"] "+p+"Install XAttacker")
       print (gt+"  ["+p+"96"+gt+"] "+p+"Install XSStrike")
       print (gt+"  ["+p+"97"+gt+"] "+p+"Install Xerosploit")
       print (gt+"  ["+p+"98"+gt+"] "+p+"Install Youtube Dl")
       print (gt+"  ["+p+"99"+gt+"] "+p+"Install Zambie")
       print (gt+"  ["+p+"100"+gt+"] "+p+"Install Zilcorili")
       slowprint (gt+"  ["+p+"999"+gt+"] "+p+"About")
       print (gt+"  ["+p+"0"+gt+"] "+p+"Keluar")
       
       
       
       choice = str(input(O+" Masukkan Pilihan "+m+": "+bt))
       exec_menu(choice)
       return
       slowprint(W + '# ' + str(time.strftime('%a, %d %B %Y')))

def exec_menu(choice):
    clear()
    if(choice == ''):
        menu_actions['main']()
    else:
        try:
            menu_actions[choice]()
        except KeyError:
            print("Invalid selection, please try again.\n")
            menu_actions['main']()
    return

def menu_1():
    slowaprint("loading...")
    os.system('apt update && apt upgrade;apt-get install php;mkdir adfin;cd ~/adfin;wget https://pastebin.com/raw/32txZ6Qr -O adfin.php;mv adfin $HOME')
    print(k+"Sudah di install gan silahkan lihat di cd $HOME"+W)

def menu_2():
    slowaprint("loading...")
    os.system('apt-get update && apt-get upgrade')
    os.system('apt-get install aircrack-ng')

def menu_3():
    slowaprint("loading...")
    system('pkg update && pkg upgrade')
    system('pkg install git')
    system('git clone https://github.com/Techzindia/admin_penal')
    system('mv admin_penal $HOME')
    print(k+"Sudah di install gan silahkan lihat di cd $HOME"+W)

def menu_4():
    slowaprint("loading...")
    os.system('apt update && apt upgrade;apt-get install git;git clone https://github.com/sdrausty/termux-archlinux.git;mv termux-archlinux $HOME')
    print(k+"Sudah di install gan silahkan lihat di cd $HOME"+W)

def menu_5():
    slowaprint("loading...")
    os.system('apt update && apt upgrade')
    os.system('apt install git')
    os.system('apt install python')
    os.system('apt install python2')
    os.system('git clone https://github.com/Gameye98/Auxscan2.0.git')
    os.system('mv Auxscan2.0 $HOME')
    print(k+"Sudah di install gan silahkan lihat di cd $HOME"+W)

def menu_6():
    slowaprint("loading...")
    os.system('apt update && apt upgrade')
    os.system('apt install git')
    os.system('apt install sh')
    os.system('pip2 install sh')
    os.system('git clone https://github.com/Gameye98/AstraNmap')
    os.system('mv AstraNmap $HOME')
    print(k+"Sudah di install gan silahkan lihat di cd $HOME"+W)
    
def menu_7():
    slowaprint("loading...")
    os.system('apt-get update && apt-get upgrade')
    os.system('apt-get install git')
    os.system('git clone git://git.kali.org/packages/bluepot.git')
    os.system('mv bluepot $HOME')
    print(k+"Sudah di install gan silahkan lihat di cd $HOME"+W)
    
def menu_8():
    slowaprint("loading...")
    os.system('apt install curl')
    os.system('apt install grep')
    os.system('apt install lynx')
    os.system('git clone https://github.com/Hood3dRob1n/BinGoo.git')
    os.system('mv BinGoo $HOME')
    os.system('cd $HOME/BinGoo')
    os.system('termux-fix-shebang bingoo')
    os.system('chmod +x bingoo')
    os.system('bash bingoo')

def menu_9():
    slowaprint("loading...")
    os.system('apt update && apt upgrade')
    os.system('apt install git')
    os.system('git clone git://git.kali.org/packages/bluemaho.git')
    os.system('mv bluemaho $HOME')
    print(k+"Sudah di install gan silahkan lihat di cd $HOME"+W)

def menu_10():
    slowaprint("loading...")
    os.system('apt install update && apt upgrade')
    os.system('apt install git')
    os.system('git clone https://github.com/Screetsec/BruteSploit')
    os.system('mv BruteSploit $HOME')
    os.system('cd $HOME/BruteSploit')
    os.system('chmod 777 Brutesploit')
    os.system('./Brutesploit')

def menu_11():
    slowaprint("loading...")
    os.system('apt update && apt upgrade')
    os.system('apt install php')
    os.system('apt install wget')
    os.system('wget https://pastebin.com/raw/tjQY6Tsg -O dorker.php')
    os.system('mv dorker.php $HOME')
    print(k+"Sudah di install gan silahkan lihat di cd $HOME"+W)

def menu_12():
    slowaprint("loading...")
    os.system('apt update && apt upgrade')
    os.system('apt install wget')
    os.system('wget http://www.morningstarsecurity.com/downloads/bing-ip2hosts-0.4.tar.gz && tar -xzvf bing-ip2hosts-0.4.tar.gz && cp bing-ip2hosts-0.4/bing-ip2hosts /usr/local/bin/t')
    print(k+"Sudah di install gan"+W)

def menu_13():
    slowaprint("loading...")
    os.system('apt update && apt upgrade')
    os.system('apt install python2')
    os.system('pip2 install colorama')
    os.system('pkg install colorama')
    os.system('pip install colorama')
    os.system('pip2 install mechanize')
    os.system('pkg install mechanize')
    os.system('pip install mechanize')
    os.system('apt install git')
    os.system('git clone https://github.com/shawarkhanethicalhacker/BruteXSS')
    os.system('mv BruteXSS $HOME')
    print(k+"Sudah di install gan silahkan lihat di cd $HOME"+W)

def menu_14():
    slowaprint("loading...")
    os.system('apt update && apt upgrade')
    os.system('apt install git')
    os.system('apt install python2')
    os.system('pip2 install requests')
    os.system('git clone https://github.com/kereh/BlackMail')
    os.system('mv BlackMail $HOME')
    print(k+"Sudah di install gan silahkan lihat di cd $HOME"+W)

def menu_15():
    slowaprint("loading...")
    os.system('apt update && apt upgrade')
    os.system('apt install python2')
    os.system('apt install git')
    os.system('git clone https://github.com/kereh/Blacktrack')
    os.system('mv Blacktrack $HOME')
    print(k+"Sudah di install gan silahkan lihat di cd $HOME"+W)

def menu_16():
    slowaprint("loading...")
    os.system('apt update && apt upgrade')
    os.system('apt install git')
    os.system('apt install python2')
    os.system('git clone https://github.com/thehackingsage/bughunter.git')
    os.system('mv bughunter $HOME')
    print(k+"Sudah di install gan silahkan lihat di cd $HOME"+W)

def menu_17():
    slowaprint("loading...")
    os.system('apt update && apt upgrade')
    os.system('apt install git')
    os.system('git clone https://github.com/Xi4u7/BlackNmap')
    os.system('mv BlackNmap $HOME')
    print(k+"Sudah di install gan silahkan lihat di cd $HOME"+W)

def menu_18():
    slowaprint("loading...")
    os.system('apt update && apt upgrade')
    os.system('apt install git')
    os.system('apt install python')
    os.system('apt install python2')
    os.system('git clone https://github.com/Gameye98/Black-Hydra.git')
    os.system('mv Black-Hydra $HOME')
    print(k+"Sudah di install gan silahkan lihat di cd $HOME"+W)

def menu_19():
    slowaprint("loading...")
    os.system('apt update && apt upgrade')
    os.system('apt install git')
    os.system('git clone https://github.com/mrcakil/cok-Rat')
    os.system('mv cok-Rat $HOME')
    os.system('cd $HOME/cok-Rat')
    os.system('unzip rat.zip')
    os.system('ls')
    print(k+"Sudah di install gan"+W)

def menu_20():
    slowaprint("loading...")
    os.system('pkg install git')
    os.system('pkg install python2')
    os.system('git clone https://github.com/mebus/cupp.git')
    os.system('mv cupp $HOME')
    print(k+"Sudah di install gan silahkan lihat di cd $HOME"+W)

def menu_21():
    slowaprint("loading...")
    os.system('pkg update && pkg upgrade')
    os.system('pkg install python2')
    os.system('pkg install git')
    os.system('git clone https://github.com/kelprmdhni/clone')
    os.system('mv clone $HOME')
    print(k+"Sudah di install gan silahkan lihat di cd $HOME"+W)

def menu_22():
    slowaprint("loading...")
    os.system('apt-get update')
    os.system('apt-get upgrade')
    os.system('pkg install python')
    os.system('apt-get install git')
    os.system('git clone https://github.com/Dionach/CMSmap.git')
    os.system('mv CMSmap $HOME')
    print(k+"Sudah di install gan silahkan lihat di cd $HOME"+W)

def menu_23():
    slowaprint("loading...")
    os.system('apt-get update && apt-get upgrade')
    os.system('apt-get install wget')
    os.system('apt-get install php')
    os.system('wget https://pastebin.com/raw/EAtSir5V -O com_foxcontact.php')
    os.system('mv com_foxcontact.php $HOME')
    print(k+"Sudah di install gan Usage: php com_foxcontact.php target.txt"+W)

def menu_24():
    slowaprint("loading...")
    os.system('apt-get update && apt-get upgrade')
    os.system('apt-get install wget')
    os.system('apt-get install php')
    os.system('wget https://pastebin.com/raw/LDvFvtUD -O com_fabrik.php')
    os.system('mv com_fabrik.php $HOME')
    print(k+"Sudah di install gan Usage: php com_fabrik.php target.txt"+W)

def menu_25():
    slowaprint("loading...")
    os.system('apt-get update && apt-get upgrade')
    os.system('pkg install python')
    os.system('apt-get install git')
    os.system('git clone https://github.com/Dionach/CMSmap.git')
    os.system('mv CMSmap $HOME')
    print(k+"Sudah di install gan silahkan lihat di cd $HOME"+W)

def menu_26():
    slowaprint("loading...")
    os.system('apt update && apt upgrade')
    os.system('apt install python git')
    os.system('python -m pip install uncompyle6')
    os.system('git clone https://github.com/KANG-NEWBIE/ComLap')
    os.system('mv ComLap $HOME')
    print(k+"Sudah di install gan silahkan lihat di cd $HOME"+W)

def menu_27():
    slowaprint("loading...")
    os.system('pkg update && pkg upgrade')
    os.system('pkg install python2')
    os.system('pkg install git')
    os.system('git clone https://github.com/Al2VyN/Compiler.git')
    os.system('mv Compiler $HOME')
    print(k+"Sudah di install gan silahkan lihat di cd $HOME"+W)

def menu_28():
    slowaprint("loading...")
    os.system('pkg update && pkg upgrade')
    os.system('pkg install git')
    os.system('pkg install python2')
    os.system('git clone https://github.com/Sazxt/comz')
    os.system('mv comz $HOME')
    print(k+"Sudah di install gan silahkan lihat di cd $HOME"+W)

def menu_29():
    slowaprint("loading...")
    os.system('apt update && apt upgrade')
    os.system('apt-get install python')
    os.system('apt-get install python2')
    os.system('apt-get install git')
    os.system('git clone https://github.com/KANG-NEWBIE/DeShal')
    os.system('mv DeShal $HOME')
    os.system('python -m pip install uncompyle6')
    os.system('python2 -m pip install uncompyle6')
    print(k+"Sudah di install gan silahkan lihat di cd $HOME"+W)

def menu_30():
    slowaprint("loading...")
    os.system('pkg update && pkg upgrade')
    os.system('pkg install python2')
    os.system('pkg install git')
    os.system('git clone https://github.com/rezadkim/dark-fb')
    os.system('mv dark-fb $HOME')
    os.system('pip2 install requests')
    os.system('pip2 install mechanize')
    print(k+"Sudah di install gan silahkan lihat di cd $HOME"+W)

def menu_31():
    slowaprint("loading...")
    os.system('apt-get update && apt upgrade')
    os.system('apt-get install python')
    os.system('apt-get install git')
    os.system('git clone https://github.com/maurosoria/dirsearch.git')
    os.system('mv dirsearch $HOME')
    print(k+"Sudah di install gan silahkan lihat di cd $HOME"+W)

def menu_32():
    slowaprint("loading...")
    os.system('apt-get update && apt-get upgrade')
    os.system('apt-get install git')
    os.system('apt-get install python2')
    os.system('git clone https://github.com/shawarkhanethicalhacker/D-TECT')
    os.system('mv D-Tect $HOME')
    print(k+"Sudah di install gan silahkan lihat di cd $HOME"+W)

def menu_33():
    slowaprint("loading...")
    os.system('apt update && apt upgrade')
    os.system('apt install python')
    os.system('apt install git')
    os.system('git clone https://github.com/UltimateHackers/Decodify')
    os.system('mv Decodify $HOME')
    print(k+"Sudah di install gan silahkan lihat di cd $HOME"+W)

def menu_34():
    slowaprint("loading...")
    os.system('pkg update && pkg upgrade')
    os.system('pkg install git')
    os.system('git clone https://github.com/4L13199/LITEDDOS')
    os.system('mv LITEDDOS $HOME')
    os.system('')
    os.system('')
    print(k+"Sudah di install gan silahkan lihat di cd $HOME"+W)

def menu_35():
    slowaprint("loading...")
    os.system('apt update')
    os.system('apt upgrade')
    os.system('apt install git')
    os.system('git clone https://github.com/Screetsec/Dracnmap')
    os.system('mv Dracnmap $HOME')
    print(k+"Sudah di install gan silahkan lihat di cd $HOME"+W)

def menu_36():
    slowaprint("loading...")
    os.system('apt update && apt upgrade')
    os.system('apt install python2')
    os.system('apt install git')
    os.system('git clone https://github.com/haijuga7/Dec-Enc-Hash')
    os.system('mv Dec-Enc-Hash $HOME')
    print(k+"Sudah di install gan silahkan lihat di cd $HOME"+W)

def menu_37():
    slowaprint("loading...")
    os.system('apt update && apt upgrade')
    os.system('apt install python2')
    os.system('apt install git')
    os.system('git clone https://github.com/zanyarjamal/DataSploit')
    os.system('mv DataSploit $HOME')
    os.system('cd $HOME/DataSploit')
    os.system('pip2 install -r requirements.txt')
    print(k+"Sudah di install gan silahkan lihat di cd $HOME"+W)

def menu_38():
    slowaprint("loading...")
    os.system('apt update')
    os.system('apt upgrade')
    os.system('apt install git')
    os.system('apt install python2')
    os.system('git clone https://github.com/maldevel/EmailHarvester')
    os.system('mv EmailHarvester $HOME')
    os.system('cd $HOME/EmailHarvester')
    os.system('pip2 install -r requirements.txt')
    print(k+"Sudah di install gan silahkan lihat di cd $HOME"+W)

def menu_39():
    slowaprint("loading...")
    os.system('apt update && apt upgrade')
    os.system('apt install git')
    os.system('git clone https://github.com/rand0m1ze/ezsploit')
    os.system('mv ezsploit $HOME')
    print(k+"Sudah di install gan silahkan lihat di cd $HOME"+W)

def menu_40():
    slowaprint("loading...")
    os.system('apt update && apt upgrade')
    os.system('apt install python2')
    os.system('apt install git')
    os.system('git clone https://gitlab.com/Sumarr-ID/Encrypt-python')
    os.system('mv Encrypt-python $HOME')
    print(k+"Sudah di install gan silahkan lihat di cd $HOME"+W)

def menu_41():
    slowaprint("loading...")
    os.system('pkg update && pkg upgrade')
    os.system('pkg install nodejs git')
    os.system('git clone https://github.com/ibnusyawall/find-shell')
    os.system('mv find-shell $HOME')
    os.system('cd $HOME/find-shell')
    os.system('npm init -y')
    os.system('npm install --save request colors shelljs readline fs')
    os.system('node index')
    print(k+"Sudah di install gan silahkan lihat di cd $HOME"+W)

def menu_42():
    slowaprint("loading...")
    os.system('pkg update && pkg upgrade')
    os.system('pkg install python2')
    os.system('pkg install git')
    os.system('git clone https://github.com/LOoLzeC/FlipTracker')
    os.system('mv FlipTracker $HOME')
    print(k+"Sudah di install gan silahkan lihat di cd $HOME"+W)

def menu_43():
    slowaprint("loading...")
    os.system('pkg update && pkg upgrade')
    os.system('pkg install php')
    os.system('pkg install git')
    os.system('git clone https://github.com/indosecid/gps_tracking')
    os.system('mv gps_tracking $HOME')
    print(k+"Sudah di install gan silahkan lihat di cd $HOME"+W)

def menu_44():
    slowaprint("loading...")
    os.system('pkg update && pkg upgrade')
    os.system('pkg install python2')
    os.system('pkg install git')
    os.system('git clone https://github.com/XG77Z10/Google-Dork')
    os.system('mv Google-Dork $HOME')
    print(k+"Sudah di install gan silahkan lihat di cd $HOME"+W)

def menu_45():
    slowaprint("loading...")
    os.system('pkg update && pkg upgrade')
    os.system('pkg install python2')
    os.system('pkg install git')
    os.system('git clone https://github.com/UltimateHackers/Hash-Buster')
    os.system('mv Hash-Buster $HOME')
    print(k+"Sudah di install gan silahkan lihat di cd $HOME"+W)

def menu_46():
    slowaprint("loading...")
    os.system('pkg update && pkg upgrade')
    os.system('pkg install python2')
    os.system('pkg install git')
    os.system('pip2 install passlib')
    os.system('git clone https://github.com/afelfgie/HashTool')
    os.system('mv HashTool $HOME')
    print(k+"Sudah di install gan silahkan lihat di cd $HOME"+W)

def menu_47():
    slowaprint("loading...")
    os.system('pkg update && pkg upgrade')
    os.system('pkg install python')
    os.system('pkg install git')
    os.system('git clone https://github.com/b3-v3r/Hunner')
    os.system('mv Hunner $HOME')
    print(k+"Sudah di install gan silahkan lihat di cd $HOME"+W)

def menu_48():
    slowaprint("loading...")
    os.system('pkg update && pkg upgrade')
    os.system('pkg install git')
    os.system('pkg install python2')
    os.system('git clone https://github.com/pirmansx/hostchecker')
    os.system('mv hostchecker $HOME')
    print(k+"Sudah di install gan silahkan lihat di cd $HOME"+W)

def menu_49():
    slowaprint("loading...")
    os.system('pkg update && pkg upgrade')
    os.system('pkg install git')
    os.system('pkg install python2')
    os.system('git clone https://github.com/haijuga7/Hashcode')
    os.system('mv Hashcode $HOME')
    print(k+"Sudah di install gan silahkan lihat di cd $HOME"+W)

def menu_50():
    slowaprint("loading...")
    os.system('pkg update && pkg upgrade')
    os.system('pkg install git')
    os.system('pkg install python')
    os.system('git clone https://github.com/m4ll0k/Infoga.git infoga')
    os.system('mv infoga $HOME')
    os.system('cd $HOME/infoga')
    os.system('pip install -r req')
    print(k+"Sudah di install gan silahkan lihat di cd $HOME"+W)

def menu_51():
    slowaprint("loading...")
    os.system('pkg update && pkg upgrade')
    os.system('pkg install git')
    os.system('pkg install python')
    os.system('git clone https://github.com/maldevel/IPGeolocation')
    os.system('mv IPGeolocation $HOME')
    os.system('cd $HOME/IPGeolocation')
    os.system('chmod +x ipgeolocation.py')
    os.system('pip install -r requirements.txt')
    print(k+"Sudah di install gan silahkan lihat di cd $HOME"+W)

def menu_52():
    slowaprint("loading...")
    os.system('pkg update && pkg upgrade')
    os.system('pkg install git')
    os.system('pkg install python')
    os.system('pkg install python2')
    os.system('git clone https://github.com/CiKu370/ipddos.git')
    os.system('mv ipddos $HOME')
    print(k+"Sudah di install gan silahkan lihat di cd $HOME"+W)

def menu_53():
    slowaprint("loading...")
    os.system('pkg update && pkg upgrade')
    os.system('pkg install git')
    os.system('git clone https://github.com/Rajkumrdusad/IP-Tracer.git')
    os.system('mv ip-IP-Tracer $HOME')
    print(k+"Sudah di install gan silahkan lihat di cd $HOME"+W)

def menu_54():
    slowaprint("loading...")
    os.system('pkg update && pkg upgrade')
    os.system('pkg install git')
    os.system('pkg install perl')
    os.system('git clone https://github.com/rezasp/joomscan.git')
    os.system('mv joomscan $HOME')
    print(k+"Sudah di install gan silahkan lihat di cd $HOME"+W)

def menu_55():
    slowaprint("loading...")
    os.system('pkg update && pkg upgrade')
    os.system('pkg install git')
    os.system('git clone https://github.com/Hax4us/Nethunter-In-Termux.git')
    os.system('mv Nethunter-In-Termux $HOME')
    os.system('cd $HOME/Nethunter-In-Termux')
    os.system('chmod 777 kalinethunter')
    print(k+"Sudah di install gan silahkan lihat di cd $HOME"+W)

def menu_56():
    slowaprint("loading...")
    os.system('pkg update && pkg upgrade')
    os.system('pkg install git')
    os.system('pkg install python2')
    os.system('git clone https://github.com/ciku370/ko-dork.git')
    os.system('mv ko-dork $HOME')
    print(k+"Sudah di install gan silahkan lihat di cd $HOME"+W)

def menu_57():
    slowaprint("loading...")
    os.system('pkg update && pkg upgrade')
    os.system('pkg install git')
    os.system('git clone https://github.com/Gameye98/Lazymux')
    os.system('mv Lazymux $HOME')
    print(k+"Sudah di install gan silahkan lihat di cd $HOME"+W)

def menu_58():
    slowaprint("loading...")
    os.system('pkg update && pkg upgrade')
    os.system('pkg install git')
    os.system('pkg install python2')
    os.system('git clone https://github.com/verluchie/termux-lazysqlmap.git')
    os.system('mv termux-lazysqlmap $HOME')
    os.system('cd $HOME/termux-lazysqlmap')
    os.system('chmod 777 install.sh')
    os.system('./install.sh')
    print(k+"Sudah di install gan silahkan lihat di cd $HOME"+W)

def menu_59():
    slowaprint("loading...")
    os.system('pkg update && pkg upgrade')
    os.system('pkg install php')
    os.system('pkg install wget')
    os.system('wget https://pastebin.com/raw/sPpJRjCZ -O lokomedia.php')
    os.system('mv lokomedia.php $HOME')
    print(k+"Sudah di install gan silahkan lihat di cd $HOME"+W)

def menu_60():
    slowaprint("loading...")
    os.system('pkg update && pkg upgrade')
    os.system('pkg install git')
    os.system('git clone https://github.com/nmilosev/termux-fedora.git')
    os.system('mv termux-fedora $HOME')
    print(k+"Sudah di install gan silahkan lihat di cd $HOME"+W)

def menu_61():
    slowaprint("loading...")
    os.system('pkg update && pkg upgrade')
    os.system('pkg install git')
    os.system('pkg install toilet')
    os.system('git clone https://github.com/4L13199/LITESPAM')
    os.system('mv LITESPAM $HOME')
    print(k+"Sudah di install gan silahkan lihat di cd $HOME"+W)

def menu_62():
    slowaprint("loading...")
    os.system('pkg update && pkg upgrade')
    os.system('pkg install git')
    os.system('pkg install php')
    os.system('git clone https://github.com/revan-ar/mail-spammer')
    os.system('mv mail-spammer $HOME')
    print(k+"Sudah di install gan silahkan lihat di cd $HOME"+W)

def menu_63():
    slowaprint("loading...")
    os.system('apt update && apt upgrade')
    os.system('apt install')
    os.system('pkg install git')
    os.system('git clone https://github.com/Rajkumrdusad/MyServer')
    os.system('mv MyServer $HOME')
    os.system('cd $HOME/MyServer')
    os.system('chmod 777 install')
    os.system('chmod +x install')
    os.system('./install')
    print(k+"Sudah di install gan silahkan lihat di cd $HOME"+W)

def menu_64():
    slowaprint("loading...")
    os.system('pkg update && pkg upgrade')
    os.system('pkg install git')
    os.system('git clone https://github.com/Screetsec/Microsploit')
    os.system('mv Microsploit $HOME')
    os.system('cd $HOME/Microsploit')
    os.system('chmod 777 Microsploit')
    os.system('./Microsploit')
    print(k+"Sudah di install gan silahkan lihat di cd $HOME"+W)

def menu_65():
    slowaprint("loading...")
    os.system('pkg install git')
    os.system('pkg install python2')
    os.system('git clone https://github.com/CiKu370/md5-crack.git')
    os.system('mv md5-crack $HOME')
    print(k+"Sudah di install gan silahkan lihat di cd $HOME"+W)

def menu_66():
    slowaprint("loading...")
    os.system('pkg update && pkg upgrade')
    os.system('pkg install git')
    os.system('git clone https://github.com/Xi4u7/NMapForAndroid')
    os.system('mv NMapForAndroid $HOME')
    print(k+"Sudah di install gan silahkan lihat di cd $HOME"+W)

def menu_67():
    slowaprint("loading...")
    os.system('apt update && apt upgrade')
    os.system('apt install git')
    os.system('apt install python')
    os.system('git clone https://github.com/zdresearch/OWASP-Nettacker')
    os.system('mv OWASP-Nettacker $HOME')
    print(k+"Sudah di install gan silahkan lihat di cd $HOME"+W)

def menu_68():
    slowaprint("loading...")
    os.system('pkg update && pkg upgrade')
    os.system('pkg install git')
    os.system('pkg install python2')
    os.system('git clone https://github.com/x3omdax/PenBox.git')
    os.system('mv PenBox $HOME')
    print(k+"Sudah di install gan silahkan lihat di cd $HOME"+W)

def menu_69():
    slowaprint("loading...")
    os.system('pkg update && pkg upgrade')
    os.system('pkg install git')
    os.system('pkg install python2')
    os.system('git clone https://github.com/the-c0d3r/port-lookup')
    os.system('mv port-lookup $HOME')
    print(k+"Sudah di install gan silahkan lihat di cd $HOME"+W)

def menu_70():
    slowaprint("loading...")
    os.system('pkg update && pkg upgrade')
    os.system('pkg install git')
    os.system('pkg install python2')
    os.system('git clone https://github.com/Dionach/reposcanner')
    os.system('mv reposcanner $HOME')
    print(k+"Sudah di install gan silahkan lihat di cd $HOME"+W)

def menu_71():
    slowaprint("loading...")
    os.system('apt install git')
    os.system('apt install python2')
    os.system('pip2 install requests')
    os.system('git clone https://github.com/reverse-shell/routersploit.git')
    os.system('mv routersploit $HOME')
    os.system('cd $HOME/cd routersploit')
    os.system('pip install -r requirements.txt')
    os.system('termux-fix-shebang rsf.py')
    print(k+"Sudah di install gan silahkan lihat di cd $HOME"+W)

def menu_72():
    slowaprint("loading...")
    os.system('pkg update && pkg upgrade')
    os.system('pkg install git')
    os.system('pkg install php')
    os.system('git clone https://github.com/Tuhinshubhra/RED_HAWK')
    os.system('mv RED_HAWK $HOME')
    print(k+"Sudah di install gan silahkan lihat di cd $HOME"+W)

def menu_73():
    slowaprint("loading...")
    os.system('pkg install git')
    os.system('pkg install python')
    os.system('pip install requests')
    os.system('git clone https://github.com/Xractz/SFile')
    os.system('mv SFile $HOME')
    print(k+"Sudah di install gan silahkan lihat di cd $HOME"+W)

def menu_74():
    slowaprint("loading...")
    os.system('apt update && apt upgrade')
    os.system('apt install python')
    os.system('apt install git')
    os.system('git clone https://github.com/KANG-NEWBIE/s-mbf')
    os.system('mv s-mbf $HOME')
    os.system('cd $HOME/s-mbf')
    os.system('python -m pip install -r req.txt')
    print(k+"Sudah di install gan silahkan lihat di cd $HOME"+W)

def menu_75():
    slowaprint("loading...")
    os.system('pkg update && pkg upgrade')
    os.system('pkg install git')
    os.system('pkg install php')
    os.system('git clone https://github.com/thelinuxchoice/saycheese')
    os.system('mv saycheese $HOME')
    print(k+"Sudah di install gan silahkan lihat di cd $HOME"+W)

def menu_76():
    slowaprint("loading...")
    os.system('pkg update && pkg upgrade')
    os.system('pkg install git')
    os.system('pkg install python2')
    os.system('git clone https://github.com/sqlmapproject/sqlmap')
    os.system('mv sqlmap $HOME')
    print(k+"Sudah di install gan silahkan lihat di cd $HOME"+W)

def menu_77():
    slowaprint("loading...")
    os.system('apt update && apt upgrade')
    os.system('apt install python2')
    os.system('apt install wget')
    os.system('mkdir scanner')
    os.system('cd $HOME/scanner')
    os.system('wget https://pastebin.com/raw/m79t1Zia -O scanner.py')
    os.system('wget https://pastebin.com/raw/mgKxMWXh -O admins.1337')
    os.system('wget https://pastebin.com/raw/EafKj98D -O files.1337')
    print(k+"Sudah di install gan. usage : python2 scanner.py site.com -m files"+W)

def menu_78():
    slowaprint("loading...")
    os.system('apt update && apt upgrade')
    os.system('apt install git')
    os.system('apt install python2')
    os.system('git clone https://github.com/shawarkhanethicalhacker/Sarahah-XSS-Exploit')
    os.system('mv Sarahah-XSS-Exploit $HOME')
    print(k+"Sudah di install gan silahkan lihat di cd $HOME"+W)

def menu_79():
    slowaprint("loading...")
    os.system('pkg update && pkg upgrade')
    os.system('pkg install git')
    os.system('pkg install python2')
    os.system('git clone https://github.com/the-c0d3r/sqli-scanner')
    os.system('mv sqli-scanner $HOME')
    print(k+"Sudah di install gan silahkan lihat di cd $HOME"+W)

def menu_80():
    slowaprint("loading...")
    os.system('apt update && apt upgrade')
    os.system('apt install python2')
    os.system('apt install python2-dev clang libxml2-dev libxml-utils libxslt-dev')
    os.system('apt install git')
    os.system('git clone https://github.com/Lexiie/sqliv.git')
    os.system('mv sqliv $HOME')
    os.system('cd $HOME/sqliv')
    os.system('pip2 install -r requirements.txt')
    os.system('python2 install setup.py -i')
    os.system('python2 sqliv.py -h')
    print(k+"Sudah di install gan silahkan lihat di cd $HOME"+W)

def menu_81():
    slowaprint("loading...")
    os.system('apt update && apt upgrade')
    os.system('apt install git')
    os.system('apt install php')
    os.system('git clone https://github.com/cyweb/server_domains')
    os.system('mv server_domains $HOME')
    print(k+"Sudah di install gan silahkan lihat di cd $HOME"+W)

def menu_82():
    slowaprint("loading...")
    os.system('pkg update && pkg upgrade')
    os.system('pkg install git')
    os.system('pkg install python')
    os.system('git clone https://github.com/cyweb/hammer')
    os.system('mv hammer $HOME')
    print(k+"Sudah di install gan silahkan lihat di cd $HOME"+W)

def menu_83():
    slowaprint("loading...")
    os.system('apt update && apt upgrade')
    os.system('apt install python2')
    os.system('apt install git')
    os.system('git clone https://github.com/4shadoww/thanatos')
    os.system('mv thanatos $HOME')
    print(k+"Sudah di install gan silahkan lihat di cd $HOME"+W)

def menu_84():
    slowaprint("loading...")
    os.system('apt update && apt upgrade')
    os.system('apt install git')
    os.system('git clone https://github.com/zanyarjamal/TrackUrl')
    os.system('mv TrackUrl $HOME')
    print(k+"Sudah di install gan silahkan lihat di cd $HOME"+W)

def menu_85():
    slowaprint("loading...")
    os.system('apt update && apt upgrade')
    os.system('apt install git')
    os.system('git clone https://github.com/Screetsec/TheFatRat.git')
    os.system('mv TheFatRat $HOME')
    os.system('cd $HOME/TheFatRat')
    os.system('chmod +x setup.sh && ./setup.sh')
    print(k+"Sudah di install gan silahkan lihat di cd $HOME"+W)

def menu_86():
    slowaprint("loading...")
    os.system('apt update && apt upgrade')
    os.system('apt install git')
    os.system('apt install wget')
    os.system('apt install proot')
    os.system('git clone https://github.com/Neo-Oli/termux-ubuntu.git')
    os.system('mv termux-ubuntu $HOME')
    os.system('cd $HOME/termux-ubuntu')
    os.system('chmod +x ubuntu.sh')
    print(k+"Sudah di install gan silahkan lihat di cd $HOME"+W)

def menu_87():
    slowaprint("loading...")
    os.system(' apt update && apt upgrade')
    os.system(' apt install git')
    os.system(' git clone https://github.com/nmilosev/anyfed')
    os.system(' mv anyfed $HOME')
    os.system(' cd $HOME/anyfed')
    os.system(' chmod 777 anyfed')
    os.system('./anyfed')
    print(k+"Sudah di install gan silahkan lihat di cd $HOME"+W)

def menu_88():
    slowaprint("loading...")
    os.system('apt update && apt upgrade')
    os.system('apt install python2')
    os.system('apt install git')
    os.system('git clone https://github.com/blackvkng/viSQL')
    os.system('mv viSQL $HOME')
    os.system('cd $HOME/viSQL')
    os.system('python2 -m pip install -r requirements.txt')
    print(k+"Sudah di install gan silahkan lihat di cd $HOME"+W)

def menu_89():
    slowaprint("loading...")
    os.system('apt update && apt upgrade')
    os.system('apt install git')
    os.system('apt install python2')
    os.system('git clone https://github.com/kereh/VulnScaner')
    os.system('mv VulnScaner $HOME')
    print(k+"Sudah di install gan silahkan lihat di cd $HOME"+W)

def menu_90():
    slowaprint("loading...")
    os.system('apt update && apt upgrade')
    os.system('apt install git')
    os.system('apt install ruby')
    os.system('apt install curl')
    os.system('git clone https://github.com/wpscanteam/wpscan')
    os.system('mv wpscan $HOME')
    os.system('cd $HOME/wpscan')
    os.system('gem install bundle')
    os.system('bundle config build.nokogiri --use-system-libraries')
    os.system('bundle install')
    os.system('ruby wpscan.rb --update')
    print(k+"Sudah di install gan silahkan lihat di cd $HOME"+W)

def menu_91():
    slowaprint("loading...")
    os.system('apt update && apt upgrade')
    os.system('apt install python2')
    os.system('apt install git')
    os.system('pip install request')
    os.system('git clone https://github.com/atarantini/wpbf')
    os.system('mv wpbf $HOME')
    print(k+"Sudah di install gan silahkan lihat di cd $HOME"+W)

def menu_92():
    slowaprint("loading...")
    os.system('apt update && apt upgrade')
    os.system('apt install python2')
    os.system('apt install git')
    os.system('git clone https://github.com/m4ll0k/WPSeku')
    os.system('mv WPSeku $HOME')
    os.system('cd $HOME/WPSeku')
    os.system('pip2 install -r requirements.txt')
    print(k+"Sudah di install gan silahkan lihat di cd $HOME"+W)

def menu_93():
    slowaprint("loading...")
    os.system('apt update && apt upgrade')
    os.system('apt install python2')
    os.system('apt install git')
    os.system('git clone https://github.com/evait-security/weeman')
    os.system('mv weeman $HOME')
    print(k+"Sudah di install gan silahkan lihat di cd $HOME"+W)

def menu_94():
    slowaprint("loading...")
    os.system('apt update && apt upgrade')
    os.system('apt install python2')
    os.system('apt install git')
    os.system('pip2 install requests')
    os.system('git clone https://github.com/Bl4ckDr460n/webdav.git')
    os.system('mv webdav $HOME')
    print(k+"Sudah di install gan silahkan lihat di cd $HOME"+W)

def menu_95():
    slowaprint("loading...")
    os.system('apt update && apt upgrade')
    os.system('apt install git')
    os.system('apt install perl')
    os.system('git clone https://github.com/Moham3dRiahi/XAttacker')
    os.system('mv XAttacker $HOME')
    os.system('cd $HOME/XAttacker')
    os.system('chmod 777 XAttacker.pl')
    print(k+"Sudah di install gan silahkan lihat di cd $HOME"+W)

def menu_96():
    slowaprint("loading...")
    os.system('apt update && apt upgrade')
    os.system('apt install git')
    os.system('apt install python')
    os.system('git clone https://github.com/UltimateHackers/XSStrike')
    os.system('mv XSStrike $HOME')
    os.system('cd $HOME/XSStrike')
    os.system(' pip install -r requirements.txt')
    print(k+"Sudah di install gan silahkan lihat di cd $HOME"+W)

def menu_97():
    slowaprint("loading...")
    os.system('apt update && apt upgrade')
    os.system('apt install python2')
    os.system('apt install git')
    os.system('git clone https://github.com/LionSec/xerosploit')
    os.system('mv xerosploit $HOME')
    print(k+"Sudah di install gan silahkan lihat di cd $HOME"+W)

def menu_98():
    slowaprint("loading...")
    os.system('apt update && apt upgrade')
    os.system('apt install python')
    os.system('pip3 install mps_youtube')
    os.system('pip3 install youtube_dl')
    os.system('apt install mpv')
    print(k+"Sudah di install gan. Untuk menjalankannya ketik 'mpsyt' tanpa tanda petik"+W)

def menu_99():
    slowaprint("loading...")
    os.system('apt update && apt upgrade')
    os.system('apt install python2')
    os.system('apt install git')
    os.system('git clone https://github.com/zanyarjamal/zambie')
    os.system('mv zambie $HOME')
    os.system('cd $HOME/zambie')
    os.system('sh Installer.sh')
    print(k+"Sudah di install gan silahkan lihat di cd $HOME"+W)

def menu_100():
    slowaprint("loading...")
    os.system('apt update && apt upgrade')
    os.system('apt install ruby')
    os.system('apt install git')
    os.system('git clone https://github.com/b3-v3r/Zilcorili')
    os.system('mv Zilcorili $HOME')
    print(k+"Sudah di install gan silahkan lihat di cd $HOME"+W)

def about():
    clear()
    slowprint(W + '-'*46)
    slowprint(W + '|    '+b+'author : N16HT_W4RR10R'+W+'                  |')
    slowprint(W + '|    '+b+'contact : t.me/N16HT_W4RR10R'+W+'            |')
    slowprint(W + '-'*46)
    print(k+"segala yang terjadi saat menggunakan tools ini ditanggu oleh pengguna\nJika terjadi error/bug harap hubungi saya")
    print(gt+"terima kasih kepada : Allah SWT, Blackode32, Unixode7, dan kepada diri saya sendiri hehe"+W)
    tanya()

def exit():
    slowaprint(k+'Loading'+p+'...')
    clear()
    print(G+"["+k+"!"+g+"] "+m+"Keluar")
    print(gt+"Sampai berjumpa lagi ;)"+W)
    sys.exit()

menu_actions = {
    "main" : main_menu,
    "1" : menu_1,
    "2" : menu_2,
    "3" : menu_3,
    "4" : menu_4,
    "5" : menu_5,
    "6" : menu_6,
    "7" : menu_7,
    "8" : menu_8,
    "9" : menu_9,
    "10" : menu_10,
    "11" : menu_11,
    "12" : menu_12,
    "13" : menu_13,
    "14" : menu_14,
    "15" : menu_15,
    "16" : menu_16,
    "17" : menu_17,
    "18" : menu_18,
    "19" : menu_19,
    "20" : menu_20,
    "21" : menu_21,
    "22" : menu_22,
    "23" : menu_23,
    "24" : menu_24,
    "25" : menu_25,
    "26" : menu_26,
    "27" : menu_27,
    "28" : menu_28,
    "29" : menu_29,
    "30" : menu_30,
    "31" : menu_31,
    "32" : menu_32,
    "33" : menu_33,
    "34" : menu_34,
    "35" : menu_35,
    "36" : menu_36,
    "37" : menu_37,
    "38" : menu_38,
    "39" : menu_39,
    "40" : menu_40,
    "41" : menu_41,
    "42" : menu_42,
    "43" : menu_43,
    "44" : menu_44,
    "45" : menu_45,
    "46" : menu_46,
    "47" : menu_47,
    "48" : menu_48,
    "49" : menu_49,
    "50" : menu_50,
    "51" : menu_51,
    "52" : menu_52,
    "53" : menu_53,
    "54" : menu_54,
    "55" : menu_55,
    "56" : menu_56,
    "57" : menu_57,
    "58" : menu_58,
    "59" : menu_59,
    "60" : menu_60,
    "61" : menu_61,
    "62" : menu_62,
    "63" : menu_63,
    "64" : menu_64,
    "65" : menu_65,
    "66" : menu_66,
    "67" : menu_67,
    "68" : menu_68,
    "69" : menu_69,
    "70" : menu_70,
    "71" : menu_71,
    "72" : menu_72,
    "73" : menu_73,
    "74" : menu_74,
    "75" : menu_75,
    "76" : menu_76,
    "77" : menu_77,
    "78" : menu_78,
    "79" : menu_79,
    "80" : menu_80,
    "81" : menu_81,
    "82" : menu_82,
    "83" : menu_83,
    "84" : menu_84,
    "85" : menu_85,
    "86" : menu_86,
    "87" : menu_87,
    "88" : menu_88,
    "89" : menu_89,
    "90" : menu_90,
    "91" : menu_91,
    "92" : menu_92,
    "93" : menu_93,
    "94" : menu_94,
    "95" : menu_95,
    "95" : menu_96,
    "97" : menu_97,
    "98" : menu_98,
    "99" : menu_99,
    "100" : menu_100,
    "999" : about,
    "0" : exit
}


if __name__ == "__main__":
    main_menu()
    