import time
from termcolor import colored
import sys
import os
import webbrowser

if os.geteuid() != 0:
    print("You must run the script as a root user or with sudo privileges.")
    sys.exit(1)

os.system("sudo systemctl start tor; service tor start")
os.system("systemctl start nginx ; service mginx start")
os.system("systemctl start nginx-ui ; service mginx-ui start")
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
print("#" * 60)
print("=" * 60)
print("TOR will be the main service provider")
print("=" * 60)
time.sleep(3)

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
time.sleep(1)

command = f"gnome-terminal -- python3 GPReports.py & gnome-terminal -- python3 Networkreports.py & gnome-terminal -- python3 Map.py & gnome-terminal -- python3 Del.py & gnome-terminal -- python3 TargetsData.py & gnome-terminal -- python3 WebStatus.py & gnome-terminal -- python3 DirectShell.py & gnome-terminal -- python3 Meta.py"
os.system(command)
url = 'http://127.0.0.1:9000'
webbrowser.open(url)
time.sleep(3)
print(f"Your Tor Domain : ")
os.system("cat /var/lib/tor/Domain/hostname")

your_data = "Hello!"
file_path = 'Data_100101.txt'
with open(file_path, 'w') as file:
    file.write(your_data)
time.sleep(5)
os.system("rm Data_100101.txt")
os.system("exit")
