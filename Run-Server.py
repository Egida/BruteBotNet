import os
import time
import subprocess

os.system("clear")
os.system("figlet -c -f ~/.local/share/fonts/figlet-fonts/3d.flf Setup... | lolcat")

Loc = input("LocalHost Port : ")

# Check if a text file with ports exists
if os.path.exists("Ports.io"):
    with open("Ports.io", "r") as file:
        lines = file.readlines()

    ports = []

    for line in lines:
        parts = line.strip().split("=")
        if len(parts) == 2:
            try:
                port = int(parts[1].strip())
                ports.append(port)
            except ValueError:
                print(f"Invalid port value: {parts[1].strip()}")
else:
    print("No 'ports.io' file found. Please enter 10 ports manually.")
    ports = []
    for i in range(1, 11):
        while True:
            try:
                port = int(input(f"Your Server Port {i} : "))
                ports.append(port)
                break
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

print("This Servers With Ports:")
print("   ")

for port in ports:
    print(f"http://bore.pub:{port}")

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
os.system("clear")
os.system("figlet -c -f ~/.local/share/fonts/figlet-fonts/3d.flf SERVER! | lolcat")

#-------------------------------------------------------------------------------------
while len(ports) < 10:
    ports.append(0)

# Specify the number of ports to use (up to 10)
num_ports_to_use = min(len(ports), 10)

# Extract the first 10 ports from the 'ports' list
ports_to_use = ports[:num_ports_to_use]

# Replace 'Port1', 'Port2', etc. with the actual ports from the list
command = f"php -S 127.0.0.1:{Loc} & gnome-terminal -- python3 Networkreports.py & gnome-terminal -- python3 Map.py & gnome-terminal -- python3 Del.py & gnome-terminal -- python3 TargetsData.py & gnome-terminal -- python3 WebStatus.py"
for i, port in enumerate(ports_to_use, start=1):
    command += f" & gnome-terminal -- ./bore local {Loc} --to bore.pub -p {port}"

os.system(command)
