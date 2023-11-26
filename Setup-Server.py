import os
import subprocess
import time
import requests
import sys

# Check for root privileges
if os.geteuid() != 0:
    print("You must run the script as a root user or with sudo privileges.")
    sys.exit(1)


# Install necessary packages
packages = ["python3-pip", "python3-socks", "php", "dbus-x11", "gnome-terminal", "lolcat","figlet"]
subprocess.run(["sudo", "apt", "update"])
subprocess.run(["sudo", "apt", "install"] + packages + ["-y"])

# Clone figlet fonts
os.makedirs("/root/.local/share/fonts/figlet-fonts/", exist_ok=True)
subprocess.run(["git", "clone", "https://github.com/xero/figlet-fonts.git", "/root/.local/share/fonts/figlet-fonts/"])
os.system("cd /root/.local/share/fonts/figlet-fonts/ ; mv 'ANSI Regular.flf' 3d.flf")
# Install Python packages
python_packages = ["folium", "geopy", "psutil", "wmi", "Dispatch", "ping3", "termcolor", "plotly", "mss", "opencv-python"]
subprocess.run(["pip", "install"] + python_packages)

# Install and start Tor
subprocess.run(["sudo", "apt", "install", "tor", "-y"])
subprocess.run(["sudo", "systemctl", "start", "tor"])
subprocess.run(["sudo", "service", "tor", "start"])

# Configure Tor Hidden Service
tor_config = """
HiddenServiceDir /var/lib/tor/Domain/
HiddenServicePort 80 127.0.0.1:8080
HiddenServicePort 80 127.0.0.1:8070
SocksPort 127.0.0.1:9150
"""
with open("/etc/tor/torrc", "a") as torrc:
    torrc.write(tor_config)
os.system("service tor restar ;systemctl restart tor")
time.sleep(5)
#subprocess.run(["sudo", "systemctl", "restart", "tor"])
#subprocess.run(["sudo", "cp", "/var/lib/tor/Domain/hostname", "."])
#subprocess.run(["sudo", "cp", "-r", "/etc/tor", "."])
#subprocess.run(["sudo", "cp", "-r", "/var/lib/tor", "."])
#os.rename("tor", "TorDomainInfo")

# Download figlet font "3d.flf"
subprocess.run(["wget", "-O", "/root/.local/share/fonts/figlet-fonts/3d.flf", "https://raw.githubusercontent.com/xero/figlet-fonts/master/ANSI%20Regular.flf"])

# Display success message
print("Installation completed!")
os.system("clear")
os.system("figlet -c -f ~/.local/share/fonts/figlet-fonts/3d.flf Restart? | lolcat")
print("Operating instructions : ")

print("=" * 40)
print("You must restart your device to start the services properly. Do you want to restart your device now? (y/n)")
print("=" * 40)
print('->>> Run "python3 Run-Server.py" to start service (after restart).')
print("=" * 40)
x = input(" >>> ")
if x == "y" or "Y":
    os.system("reboot")
else:
    print("You must restart your device to start the services properly. If you previously restarted your device after installing the program, you can continue.")
time.sleep(5)
