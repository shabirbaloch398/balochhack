
import time,os,sys
from termcolor import colored

os.system("clear")
print(colored("                 <<<<<(WELCOME TO 'Baloch' DEVELOPEMENT.)>>>>>","yellow"))
time.sleep(1.5)
os.system("clear")

try:
	print(colored("""

{
                                                     
########                                                     
##      ## *************************************             
#       ##    __Tutorial/Channel__[youtube.com/UCRnpWUOCz3Sb1RAX3GK4r0A]
########                                                     
########                                                     
#       ##    __Repository__[https://github.com/shabirbaloch398/]  
##      ##    __Author_Name__[MR Shabir Baloch]                 
########_______________}                                     
                                                             
_________                    ________________________________
                                        Love you Pakistan           
                                           V1.0 """          
,"""blue"""))
	time.sleep(0.6)
	class gh:
		
		group=input(colored("\n[?] Group id: ","cyan"))
		user=input(colored("[?] User id: ","cyan"))
		def ui(self):
			if not len(self.user)>13:
				print(colored("[!] Invalid user id.","red"))
				sys.exit()
			else:
				os.system("clear")
				print(colored("Adding.","green"))
				time.sleep(0.5)
				os.system("clear")
				print(colored("Adding..","yellow"))
				time.sleep(0.5)
				os.system("clear")
				print(colored("Adding...","cyan"))
				os.system("clear")
				print(colored("Adding.","green"))
				time.sleep(0.5)
				os.system("clear")
				print(colored("Adding..","yellow"))
				time.sleep(0.5)
				os.system("clear")
				print(colored("Adding...","cyan"))
				time.sleep(1.7)
				os.system("clear")
				print(colored("[!] Congratulation !","blue"))
				print(colored(f"[! NOTE:]   Copy Link, And Send To Admin","yellow"))
				print(colored(f"       https://m.facebook.com/group/add_admin/?group_id={self.group}&user_id={self.user}&added&_rdrChange$","green"))
				print(colored(f"\n *******************************************************************************************************************","red"))
		#user=input(colored("[?] User id: ","cyan"))
		def gi(self):
			if not len(self.group)>13:
				print(colored("[!] Invalid group id.","red"))
				sys.exit()
except KeyboardInterrupt:
	ex=input(colored("\n[?] Did you just try to quit application ? Y/n: ","yellow"))
	if ex=="y" or ex=="Y":
		print(colored("[!] Thank you for using 'fbg-hack-eb' .","cyan"))
		time.sleep(1)
		print(colored("[!] Quiting the application.","red"))
		time.sleep(2)
		sys.exit(colored("[!] done !","yellow"))
	else:
		sys.exit(colored("\n[!] Sorry, You are disconnected already.","red"))
ghi=gh()
ghi.gi()
ghi.ui()
	
	
