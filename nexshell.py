import os, socket, sys, platform

try:
    import colorama
except ImportError:
    print("Installing colorama...")
    os.system('cmd /c "pip install colorama"')
    import colorama

try:
    import webbrowser
except ImportError:
    print("Installing webbrowser...")
    os.system('cmd /c "pip install webbrowser"')
    import webbrowser
       
try:
    from uptime import uptime
    import time
except ImportError:
    print("Installing uptime...")
    os.system('cmd /c "pip install uptime"')
    from uptime import uptime
    import time
    
from colorama import Fore, Back, Style
os.system('cmd /c "cls"')

maincolor = Fore.CYAN

shellver = "1.1"

print(maincolor)

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
print("Welcome to NEXShell " + shellver + ", " + username + "!") 
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
    elif shell == " ":  
                        print(" ")
                        print("Nice void.")
                        print(" ")
    elif shell == "":   
                        print(" ")
                        print("Please type a command...")
                        print(" ")
    elif shell == "nfetch":
                        print(" ")
                        print("Please type a command...")
                        print(" ")                    
    
    elif shell == "dir":
                        print("Dir Is deprecated in NEXShell, please use ls insted") 
                        
    elif shell == "shellver":
                        print(shellver)
                        
    elif shell == "a command":
                        print(" ")
                        print("Very funny, " + username + ".")  
                        print(" ")
    elif shell == "ls":
                        os.system('cmd /c "@echo off & dir & @echo on"')                                  
    elif shell == "help":
                        print("----=================================----")
                        print("NEXShell built in commands:")
                        print("fetchit - Works like neofetch, Print's BASIC system information.")
                        print("ncalc - Simple calculator.")
                        print("help - Print's this help screen.")
                        print("cmdhelp - Print's the cmd help screen.")
                        print("sdr - Works like cd, switches your working directory")
                        print("update - Help's update NEXShell")
                        print("shellver - Print's Current shell's version")
                        print("github - Brings you to the NEXShell github page.")
                        print("clear - Clears all recent commands on screen.")
                        print("ls - Lists all content in current directory.")         
                        print("exit - Exit NEXShell.")
                        print("----=================================----")
    elif shell == "fetchit":
                        print(Fore.CYAN + "                                ..,   " + Fore.GREEN + username + "<@>" + hostname)
                        print(Fore.CYAN + "                    ....,,:;+ccllll   " + Fore.WHITE + "---================---")
                        print(Fore.CYAN + "      ...,,+:;  cllllllllllllllllll " + Fore.GREEN +  "OS: " + Fore.CYAN + platform.system() + " " + platform.release())
                        print(Fore.CYAN + ",cclllllllllll  lllllllllllllllllll " + Fore.GREEN +  "Kernel: " + Fore.BLUE + platform.version())
                        print(Fore.CYAN + "llllllllllllll  lllllllllllllllllll " + Fore.GREEN +  "Uptime: " + Fore.RED + time.strftime('%H Hours, ' + Fore.GREEN + '%M Minutes, ' + Fore.BLUE + '%S Seconds', time.gmtime(uptime())))
                        print(Fore.CYAN + "llllllllllllll  lllllllllllllllllll " + Fore.GREEN +  "Shell: " + Fore.CYAN + "NEXShell " + maincolor + shellver)
                        print(Fore.CYAN + "llllllllllllll  lllllllllllllllllll ")
                        print(Fore.CYAN + "llllllllllllll  lllllllllllllllllll ")
                        print(Fore.CYAN + "llllllllllllll  lllllllllllllllllll ")
                        print(Fore.CYAN + "                                    ")
                        print(Fore.CYAN + "llllllllllllll  lllllllllllllllllll ")
                        print(Fore.CYAN + "llllllllllllll  lllllllllllllllllll ")
                        print(Fore.CYAN + "llllllllllllll  lllllllllllllllllll ")
                        print(Fore.CYAN + "llllllllllllll  lllllllllllllllllll ")
                        print(Fore.CYAN + "llllllllllllll  lllllllllllllllllll ")
                        print(Fore.CYAN + "`'ccllllllllll  lllllllllllllllllll ")
                        print(Fore.CYAN + "       `' \*::  :ccllllllllllllllll ")
                        print(Fore.CYAN + "                       ````''*::cll ")
                        print(Fore.CYAN + "                                 `` ")
                        print(maincolor)
    elif shell == "cmdhelp":
                        os.system('cmd /c "help"')
    elif shell == "cd":
                        print("Cd breaks when running under NEXShell, therefore it is disabled while the shell is running.")
                        print("Please use the sdr command")
    elif shell == "update":
                        print(Fore.RED + "WARNING: This will not work if you are not running as Administrator.")
                        print(Fore.RED + "The update command also only works on windows 10 17063 and newer.")
                        print(maincolor + "Please specify the directory the update zip file is in...")
                        updatedir = input()
                        os.system('cmd /c tar -xf ' + updatedir)
                        os.system('cmd /c copy /Y "NEXShell-main\" "C:\Windows\System32"')
                        print(Fore.GREEN + "The update should be done, Please restart NEXShell.")
                        print(Fore.GREEN + "NEXShell will now exit now, Thank you for updating! And goodbye.")
                        print(maincolor + " ")
                        os.system("pause")
                        print(Fore.WHITE)
                        exit()                    
    elif shell == "sdr":
                        print("----=================================----")
                        godir = input("Please enter the directory now ~> ")
                        os.chdir(godir)
    elif shell == "github":
                        print(" ")
                        print(Fore.GREEN + "Bringing you to the NEXShell github page...")
                        print(Fore.GREEN + "A Web browser window will now open.")
                        webbrowser.open('https://github.com/Nex320/NEXShell')
                        print(maincolor)
                                            
                        
    elif shell == "clear":
                        print(maincolor)
                        os.system('cmd /c "cls"')                       
                        print("----=================================----")
                        print("     NN     N   EEEEEEEE   X       X")
                        print("     N N    N   EE           X   X  ")
                        print("     N  NN  N   EEEEE          X    ")
                        print("     N    N N   EE           X   X  ")
                        print("     N     NN   EEEEEEEE   X       X")
                        print("----=================================----")
                        print("              NEXShell " + shellver)
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
                        print(maincolor)
                        