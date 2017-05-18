
import socket
import subprocess
import time
import os, re

def isActive() :
    pc_name = socket.gethostname()
    address = (pc_name, 445)
    mySoc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try :
        mySoc.connect(address)
        return True
    except Exception as e :
        if "[WinError 10061]" in str(e) :
            return False

def findPID(port = 445) :
    out_bytes = subprocess.check_output(['netstat','-ano'])
    data = out_bytes.decode().split("\r\n\r\n")[1].split("\r\n")
    regex = re.compile(":445.+ (\d*)")
    for process in data :
        if ":445" in process :
            pid = regex.search(process)
            yield pid.groups()[0]

def closePort() :
    for pid in findPID() :
        try :
            os.system("taskkill /F /PID {}".format(pid))
        except Exception as e :
            print("Port {} couldnt be killer because".format(pid))
            print(e)
            input()
        
for i in range(5) :
    if isActive() :
        closePort()
        print("Trying again in 2 secounds. -- {}\n\n".format(i))
        time.sleep(2)
    else :
        print("Port 445 has been closed succesfully")
        input("Enter any key to continue ... ")
        break

if isActive() :
    print("Port 445 ccouldnt be closed !!!")
    input("Enter any key to continue ... ")
        



