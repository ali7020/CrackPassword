

#####_______________A little python script to crack the Password_______________#####

#####=============== The libraies used in this script ===============#####

import sys

import subprocess as ps

import cowsay

from random import*

from colorama import init, AnsiToWin32, Fore, Back

from datetime import datetime
from pyfiglet import Figlet


tem = ps.call("cls",shell=True)#Ues the word("clear")for Linux!!

init(wrap=False)
stream = AnsiToWin32(sys.stderr).stream
print(Fore.MAGENTA,"",file=stream)
cowsay.daemon("CrackPassword")
print()
Text=Figlet(font="slant")
print(Text.renderText("CrackPassword"))
print(Fore.MAGENTA,"",file=stream)
print(Fore.GREEN,"||========================== YOU WELCOME ===========================||",file=stream)
print()
print(Fore.RED,"||\t\tMR.A.RAEISI_ MY_city_Nikshahr                        ||",file=stream)
print()
print(Fore.YELLOW,"||\t\t\t     IRAN                                    ||",file=stream)
print()
print(Fore.CYAN,"||\t\t@EMAIL: Raisi702000@gmail.com                        ||",file=stream)
print()
print(Fore.GREEN,"||==========================Source Code ============================||",file=stream)
print()

print(Fore.MAGENTA,"",file=stream)
user_pass= input("\t\t\tEnter Your passpowrd: ")
print(Fore.MAGENTA,"",file=stream)

print(Fore.RED,"_"*70,file=stream)
print()
print(Fore.BLUE,"\tThe script is cracking the desired Password.....",file=stream)
print()
print(Fore.RED,"_"*70,file=stream)


password=["a","b","c","d","e","f","g","h","i","j","k","o","r","s","t","p",
          "u","m","n","v","l","y","w","q","x","z",1,2,3,4,5,6,7,8,9,0,"@",
          "_","-","!","#","&",]
guess=""

Time1 = datetime.now()
 
while (guess != user_pass):
    guess=""


    for letter in range(len(user_pass)):
        guess_letter=password[randint(0, 41)]
        guess= str(guess_letter) + str(guess)
    print(Fore.YELLOW,guess,file=stream)

print()
Time2 = datetime.now()
Total = Time2-Time1
print("||=============================== OUTPUT ========================================||")
print()
print(Fore.GREEN,"\tYour password is:====>> DateTime:",Total,"----> Pasword:" ,guess,file=stream)
print()
print(Fore.MAGENTA,"\t\t   The desired password crack was done!!",file=stream)
print()
print(Fore.YELLOW,"\t\twishing you a successful day//GOD BLess YOu!!",file=stream)
print()
print("||============================= GODBye_The END====================================||")

