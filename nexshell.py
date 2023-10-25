import os, socket, sys, platform


if not platform.system() == "Windows":
                        print("----=================================----")
                        print("     NN     N   EEEEEEEE   X       X")
                        print("     N N    N   EE           X   X  ")
                        print("     N  NN  N   EEEEE          X    ")
                        print("     N    N N   EE           X   X  ")
                        print("     N     NN   EEEEEEEE   X       X")
                        print("----=================================----")
                        print("         NEXShell Critical Error.        ")
                        print("----=================================----")
                        print(" ")
                        print("> NEXShell has failed to load!")
                        print("> This is probably due to the user attempting to run it on a non-windows platform.")
                        print("> ERROR CODE: 1x0")
                        print(" ")

                        exit()     
                        
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

shellver = "1.4"

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
print("  Welcome to NEXShell " + shellver + ", " + username + "!") 
print("----=================================----")

while True:
    directory = os.getcwd()
    print("╔" + username + "<@>" + hostname)
    shell = input("╚" + directory + " ~> ")
    sharray = shell.split(" ")
    
    if "exit" in sharray[0]:
                        print(maincolor)
                        os.system('cmd /c "cls"')                       
                        print("----=================================----")
                        print("     NN     N   EEEEEEEE   X       X")
                        print("     N N    N   EE           X   X  ")
                        print("     N  NN  N   EEEEE          X    ")
                        print("     N    N N   EE           X   X  ")
                        print("     N     NN   EEEEEEEE   X       X")
                        print("----=================================----")
                        print("                Goodbye!")
                        print("----=================================----")
                        print(Fore.WHITE)
                        sys.exit()
    elif "cls" in sharray[0]: 
                        print("Cls Is deprecated in NEXShell, please use \"clear\" insted")
    elif shell == " ":  
                        print(" ")
                        print("Nice void.")
                        print(" ")
    elif shell == "":   
                        print(" ")
                        print("Please type a command...")
                        print(" ")
    elif "dir" in sharray[0]:
                        print("Dir Is deprecated in NEXShell, please use \"ls\" insted") 
                        
    elif "shellver" in sharray[0]:
                        print(" ")
                        print("Shellver: " + shellver)
                        print(" ")
                        
    elif "a command" in sharray[0]:
                        print(" ")
                        print("Very funny, " + username + ".")  
                        print(" ")
    elif "ls" in sharray[0]:
                        print(" ")
                        os.system('cmd /c "@echo off & dir & @echo on"') 
                        
    elif "help" in sharray[0]:
                        print("----=================================----")
                        print("NEXShell built in commands:")
                        print("zetafetch - Works like neofetch, Print's BASIC system information.")
                        print("ncalc - Simple calculator.")
                        print("help - Print's this help screen.")
                        print("cmdhelp - Print's the cmd help screen.")
                        print("sdr - Works like cd, switches your working directory.")
                        print("update - NEXShell update package installer.")
                        print("shellver - Print's Current shell's version.")
                        print("github - Brings you to the NEXShell github page.")
                        print("clear - Clears all recent commands on screen.")
                        print("ls - Lists all content in current directory.")
                        print("exit - Exit NEXShell.")
                        print("----=================================----")
    elif "fetchit" in sharray[0]:
                        print(" ")
                        print("Did you mean \"zetafetch\" ?")
                        print(" ")
    elif "zetafetch" in sharray[0]:
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
                        print(Fore.BLUE + "   Z e t a f e t c h  -  2 0 2 2")
                        print(maincolor)
    elif "cmdhelp" in sharray[0]:
                        os.system('cmd /c "help"')
    elif "cd" in sharray[0]:
                        print("Cd breaks when running under NEXShell, therefore it is disabled while the shell is running.")
                        print("Please use the \"sdr\" command")
    elif "update" in sharray[0]:
                        os.system('cmd /c "cls"')
                        print(maincolor + "----=================================----")
                        print("     NN     N   EEEEEEEE   X       X")
                        print("     N N    N   EE           X   X  ")
                        print("     N  NN  N   EEEEE          X    ")
                        print("     N    N N   EE           X   X  ")
                        print("     N     NN   EEEEEEEE   X       X")
                        print("----=================================----")
                        print("       Welcome to NEXShell Update!       ") 
                        print("----=================================----")
                        print(" ")
                        print(Fore.RED + "WARNING: This will not work if you are not running as Administrator.")
                        print(Fore.RED + "The update command also only works on windows 10 17063 and newer.")
                        print(maincolor + "Please specify the directory of the .nupd update package, Or type \"cancel\" to cancel.")
                        updatedir = input(Fore.GREEN + ">> ")
                        if updatedir == "cancel":
                            os.system('cmd /c "cls"')
                            print(maincolor + "----=================================----")
                            print("     NN     N   EEEEEEEE   X       X")
                            print("     N N    N   EE           X   X  ")
                            print("     N  NN  N   EEEEE          X    ")
                            print("     N    N N   EE           X   X  ")
                            print("     N     NN   EEEEEEEE   X       X")
                            print("----=================================----")
                            print("              NEXShell " + shellver)
                            print("----=================================----")
                            print(" ")
                            print(Fore.RED + "You have chose to cancel the update...")
                            print(maincolor)
                            
                        if not updatedir == "cancel":
                            os.system('cmd /c tar -xvf ' + updatedir)
                            os.system('cmd /c copy /Y "project-glasswater\" "C:\Windows\System32"')
                            os.system('del /f /q project-glasswater')
                            os.system('cmd /c "cls"')
                            print(maincolor + "----=================================----")
                            print("     NN     N   EEEEEEEE   X       X")
                            print("     N N    N   EE           X   X  ")
                            print("     N  NN  N   EEEEE          X    ")
                            print("     N    N N   EE           X   X  ")
                            print("     N     NN   EEEEEEEE   X       X")
                            print("----=================================----")
                            print("         NEXShell Update wizard.         ") 
                            print("----=================================----")
                            print(" ")
                            print(Fore.GREEN + "The update should be done, Please restart NEXShell.")
                            print(Fore.GREEN + "NEXShell will now exit now, Thank you for updating! And goodbye.")
                            print(maincolor)
                            os.system("pause")
                            print(Fore.WHITE)
                            exit() 
                        
    elif "sdr" in sharray[0]:
                        try: 
                            os.chdir(sharray[1])
                        except OSError:
                            print(Fore.RED + "Invalid Directory.")  
                            print(maincolor)
                        except IndexError:
                            print(Fore.RED + "Please Enter A Directory.")  
                            print(maincolor)
                        
        
    elif "github" in sharray[0]:
                        print(" ")
                        print(Fore.GREEN + "Bringing you to the NEXShell github page...")
                        print(Fore.GREEN + "A Web browser window will now open.")
                        webbrowser.open('https://github.com/Nex320/NEXShell')
                        print(maincolor)
                                            
                        
    elif "clear" in sharray[0]:
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
    elif "ncalc" in sharray[0]:
                        print("--===NCalculator===--")
                        print("Type exit to exit.")
                        while True:
                                calc = input(">> ")
                                if calc == "exit":
                                        break
                                else: print(eval(calc))
    else:
                        print(Fore.WHITE)
                        os.system(shell)
                        print(maincolor)                
