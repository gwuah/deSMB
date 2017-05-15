
import socket
import subprocess
import os

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
	data = out_bytes.decode().split("\r\n\r\n").split("\r\n")
	regex = re.compile(":445.+ (\d*)")
	pids = []
	for process in data :
		if ":445" in process :
			pid = regex.search(process)
			pids.append(pid)
	return True 

def closePort() :
	for pid in pids :
		try :
		     y = os.system("taskkill /F /PID 388")
		    print("done")
		    input()
		except Exception as e :
		    print(e)
		    input()



