import time
from termcolor import colored
import sys
import os

time.sleep(0.5)
os.system("clear")
os.system("figlet -c -f ~/.local/share/fonts/figlet-fonts/3d.flf Setup. | lolcat")
time.sleep(0.5)
os.system("clear")
os.system("figlet -c -f ~/.local/share/fonts/figlet-fonts/3d.flf Setup.. | lolcat")
time.sleep(0.5)
os.system("clear")
os.system("figlet -c -f ~/.local/share/fonts/figlet-fonts/3d.flf Setup... | lolcat")
print("=" * 60)
Loc = "8080"
print("LocalHost Port 8080")
print("=" * 60)
print("")
print("=" * 60)
print("TOR will be the main service provider")
print("=" * 60)
os.system("cd ~/ ;sudo systemctl restart tor ;sudo service tor restart ;sudo cp /var/lib/tor/Domain/hostname . ;sudo cp /etc/tor .;sudo cp /var/lib/tor .;mv tor TorDomainInfo")
time.sleep(2)

for _ in range(1):
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
os.system("clear")
os.system("figlet -c -f ~/.local/share/fonts/figlet-fonts/3d.flf SERVER! | lolcat")

os.system(f"""sudo echo "HiddenServiceDir /var/lib/tor/Domain/
HiddenServicePort 80 127.0.0.1:{Loc}" | sudo tee -a /etc/tor/torrc""")
time.sleep(1)
os.system("sudo systemctl restart tor; service tor restart")
time.sleep(2)

command = f"gnome-terminal -- php -S 127.0.0.1:{Loc} & gnome-terminal -- python3 Networkreports.py & gnome-terminal -- python3 Map.py & gnome-terminal -- python3 Del.py & gnome-terminal -- python3 TargetsData.py & gnome-terminal -- python3 WebStatus.py & gnome-terminal -- python3 DirectShell.py & gnome-terminal -- python3 Meta.py"
os.system(command)
time.sleep(3)
X = os.system("cat /var/lib/tor/Domain/hostname")
print(f"Your Tor Domain : {X}")
time.sleep(5)
os.system("exit")
