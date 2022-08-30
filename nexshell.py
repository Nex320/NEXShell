import os, socket, sys, platform
try:
    import colorama
except ImportError:
    print("Installing colorama...")
    os.system('cmd /c "pip install colorama"')
    import colorama
from colorama import Fore, Back, Style
os.system('cmd /c "cls"')

print(Fore.CYAN)

username = os.getlogin()
hostname = socket.gethostname()
os.system('cmd /c "cls"')
print("----=================================----")
print("     NN     N   EEEEEEEE   X       X")
print("     N N    N   EE           X   X  ")
print("     N  NN  N   EEEEE          X    ")
print("     N    N N   EE           X   X  ")
print("     N     NN   EEEEEEEE   X       X")
print("----=================================----")
print("Welcome to NEXShell v1.0, " + username + "!") 
print("----=================================----")

while True:
    directory = os.getcwd()
    print("╔" + username + "<@>" + hostname)
    shell = input("╚" + directory + " ~> ")
    
    if shell == "exit":
                        print("Goodbye.")
                        print(Fore.WHITE)
                        sys.exit()
    elif shell == "cls":
                        print("Cls Is deprecated in NEXShell, please use clear insted")
    elif shell == "dir":
                        print("Dir Is deprecated in NEXShell, please use ls insted")                    
    elif shell == "ls":
                        os.system('cmd /c "@echo off & dir & @echo on"')                                  
    elif shell == "help":
                        print("----=================================----")
                        print("NEXShell built in commands:")
                        print("sysinfo - Print system information.")
                        print("ncalc - Simple calculator.")
                        print("help - Print's this help screen.")
                        print("cmdhelp - Print's the cmd help screen.")
                        print("sdr - Works like cd, switches your working directory")
                        print("clear - Clears all recent commands on screen.")
                        print("ls - Lists all content in current directory.")         
                        print("exit - Exit NEXShell.")
                        print("----=================================----")
    elif shell == "sysinfo":
                        print("NEXShell v1.0")
                        print("Running on " + platform.system())
    elif shell == "cmdhelp":
                        os.system('cmd /c "help"')
    elif shell == "cd":
                        print("Cd breaks when running under NEXShell, therefore it is disabled while the shell is running.")
                        print("Please use the sdr command")
    elif shell == "sdr":
                        print("----=================================----")
                        godir = input("Please enter the directory now ~> ")
                        os.chdir(godir)
                        
    elif shell == "clear":
                        print(Fore.CYAN)
                        os.system('cmd /c "cls"')                       
                        print("----=================================----")
                        print("     NN     N   EEEEEEEE   X       X")
                        print("     N N    N   EE           X   X  ")
                        print("     N  NN  N   EEEEE          X    ")
                        print("     N    N N   EE           X   X  ")
                        print("     N     NN   EEEEEEEE   X       X")
                        print("----=================================----")
                        print("              NEXShell v1.0             ") 
                        print("----=================================----")
    elif shell == "ncalc":
                        print("--===NCalculator===--")
                        print("Type exit to exit.")
                        while True:
                                calc = input(">> ")
                                if calc == "exit":
                                        break
                                else: print(eval(calc))
    else:
                        print(Fore.WHITE)
                        os.system('cmd /c' + shell)
                        print(Fore.CYAN)
                        