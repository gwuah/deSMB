import subprocess
import winreg, time

__author__ = 'Griffith'

baseValues = { "dependency" : ['bowser', 'mrxsmb20', 'nsi'], "permissionError" : "[WinError 5] Access is denied" }

stationKey = winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, "SYSTEM\\CurrentControlSet\\services\\LanmanWorkstation")
key = winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, "SYSTEM\\CurrentControlSet\\services\\mrxsmb10")
defValue = winreg.QueryValueEx(key, 'Start')[0]

def dontWannaCry() : 
	winreg.SetValueEx(key, 'Start', 0, winreg.REG_DWORD, 4)

def SMB_1() :
	_key = winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, "SYSTEM\\CurrentControlSet\\Services\\LanmanServer\\Parameters")
	winreg.SetValueEx(_key, 'SMB1', 0, winreg.REG_DWORD, 0)

def setNewDependency() :
	dependency = winreg.QueryValueEx(stationKey, 'DependOnService')
	if dependency != baseValues["dependency"] :
		winreg.SetValueEx(stationKey, 'DependOnService', 0, winreg.REG_MULTI_SZ, baseValues["dependency"])
	else : pass

def main() :
	print("\nSetting New Dependencies")
	try:
		setNewDependency()
		dontWannaCry()
		SMB_1()
		print("SMB-1 has been disabled succesfully.! [STAY SAFE]")
	except Exception as e:
		if str(e) == baseValues["permissionError"] :
			print("You Cannot Disable SMB-1 Because You're Not Running Your Current Session As An Administrator")
			print("Fire Up PowerShell In Adminstrator Mode and Re-Run The Script...")
	finally:
		input("Press Any Key To Continue")

if __name__ == '__main__':
	print("Checking If You're Vulnerable ...\n")
	time.sleep(1)
	if (defValue == 2 ) or (defValue == 1 ):
		print("Your Computer Is Vulnerable!!")
		print("Patching ..")
		time.sleep(1)
		main()
	else :
		print("You're a free man \nGo and sin no more!:)")
		input("\nPress Any Key To Continue ..")
		
