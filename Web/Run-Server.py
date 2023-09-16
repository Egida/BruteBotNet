import sys
import os
import time
import subprocess
os.system("clear")
os.system("figlet -c -f ~/.local/share/fonts/figlet-fonts/3d.flf Setup... | lolcat")

print("   ")
Loc = input("Your Local Port : ")
Port = input("Your Server Port : ")

print(f"Your domain is :")

print(f"http://bore.pub:{Port}")
time.sleep(3)

os.system("clear")
os.system("figlet -c -f ~/.local/share/fonts/figlet-fonts/3d.flf Running. | lolcat")
time.sleep(0.5)
os.system("clear")
os.system("figlet -c -f ~/.local/share/fonts/figlet-fonts/3d.flf Running.. | lolcat")
time.sleep(0.5)
os.system("clear")
os.system("figlet -c -f ~/.local/share/fonts/figlet-fonts/3d.flf Running... | lolcat")
time.sleep(0.5)
os.system("clear")
os.system("figlet -c -f ~/.local/share/fonts/figlet-fonts/3d.flf Running. | lolcat")
time.sleep(0.5)
os.system("clear")
os.system("figlet -c -f ~/.local/share/fonts/figlet-fonts/3d.flf Running.. | lolcat")
time.sleep(0.5)
os.system("clear")
os.system("figlet -c -f ~/.local/share/fonts/figlet-fonts/3d.flf Running... | lolcat")
time.sleep(0.5)
#-------------------------------------------------------------------------------------
os.system(f"php -S 127.0.0.1:{Loc} & sleep 2 ; ./bore local {Loc} --to bore.pub -p {Port} & gnome-terminal -- python3 Networkreports.py & gnome-terminal -- python3 Map.py & gnome-terminal -- python3 Del.py")
