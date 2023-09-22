import os
import time
from termcolor import colored
import sys

def safe_input(prompt):
    try:
        return input(prompt)
    except UnicodeDecodeError:
        print("Invalid input. Please enter valid characters.")
        return safe_input(prompt)

os.system("clear")
os.system("figlet -c -f ~/.local/share/fonts/figlet-fonts/3d.flf Setup... | lolcat")
Loc = safe_input("LocalHost Port : ")
print("Choose your connectivity service provider:")
print("1 - BORE")
print("2 - SERVEO")
print("3 - SERVEO Domain")
SERVICE = safe_input("Choose (1, 2, or 3): ")

ports = []

if SERVICE == "1" or SERVICE == "2":
    if os.path.exists("Ports.io"):
        with open("Ports.io", "r") as file:
            lines = file.readlines()

        for line in lines:
            parts = line.strip().split("=")
            if len(parts) == 2:
                try:
                    port = int(parts[1].strip())
                    ports.append(port)
                except ValueError:
                    print(f"Invalid port value: {parts[1].strip()}")
    else:
        print("No 'Ports.io' file found. Please enter 10 ports manually.")
        for i in range(1, 11):
            while True:
                try:
                    port = int(safe_input(f"Enter Server Port {i}: "))
                    ports.append(port)
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid integer.")
        
        with open("Ports.io", "w") as file:
            for i, port in enumerate(ports, start=1):
                file.write(f"Port{i}={port}\n")

print("This Servers With Ports:")
print("   ")

if SERVICE == "1":
    for port in ports:
        print(f"http://bore.pub:{port}")
elif SERVICE == "2":
    for port in ports:
        print(f"https://serveo.net:{port}")
elif SERVICE == "3":
    DOM = safe_input("Enter Your Domain: ")
    print(f"https://{DOM}.serveo.net")
else:
    print("Invalid choice. The script will be closed and must be restarted.")
    sys.exit()

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

if SERVICE == "1":
    while len(ports) < 10:
        ports.append(0)

    num_ports_to_use = min(len(ports), 10)
    ports_to_use = ports[:num_ports_to_use]

    command = f"php -S 127.0.0.1:{Loc} & gnome-terminal -- python3 Networkreports.py & gnome-terminal -- python3 Map.py & gnome-terminal -- python3 Del.py & gnome-terminal -- python3 TargetsData.py & gnome-terminal -- python3 WebStatus.py"
    for i, port in enumerate(ports_to_use, start=1):
        command += f" & gnome-terminal -- ./bore local {Loc} --to bore.pub -p {port}"
    os.system(command)
elif SERVICE == "2":
    while len(ports) < 10:
        ports.append(0)

    num_ports_to_use = min(len(ports), 10)
    ports_to_use = ports[:num_ports_to_use]

    command = f"php -S 127.0.0.1:{Loc} & gnome-terminal -- python3 Networkreports.py & gnome-terminal -- python3 Map.py & gnome-terminal -- python3 Del.py & gnome-terminal -- python3 TargetsData.py & gnome-terminal -- python3 WebStatus.py"
    for i, port in enumerate(ports_to_use, start=1):
        command += f" & gnome-terminal -- ssh -R {port}:localhost:{Loc} serveo.net"
    os.system(command)
elif SERVICE == "3":
    command = f"php -S 127.0.0.1:{Loc} & gnome-terminal -- python3 Networkreports.py & gnome-terminal -- python3 Map.py & gnome-terminal -- python3 Del.py & gnome-terminal -- python3 TargetsData.py & gnome-terminal -- python3 WebStatus.py"
    command += f" & gnome-terminal -- ssh -R {DOM}:80:localhost:{Loc} serveo.net"
    os.system(command)
else:
    print("Invalid choice. The script will be closed and must be restarted.")
