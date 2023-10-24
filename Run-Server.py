import os
import subprocess
import time
import requests

# Install necessary packages
packages = ["python3-pip", "python3-socks", "php", "dbus-x11", "gnome-terminal"]
subprocess.run(["sudo", "apt", "update"])
subprocess.run(["sudo", "apt", "install"] + packages + ["-y"])

# Clone figlet fonts
os.makedirs("~/.local/share/fonts/figlet-fonts/", exist_ok=True)
subprocess.run(["git", "clone", "https://github.com/xero/figlet-fonts.git", "~/.local/share/fonts/figlet-fonts/"])
os.system("cd ~/.local/share/fonts/figlet-fonts/ ; mv 'ANSI Regular.flf' Reg.flf")
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

time.sleep(5)
#subprocess.run(["sudo", "systemctl", "restart", "tor"])
#subprocess.run(["sudo", "cp", "/var/lib/tor/Domain/hostname", "."])
#subprocess.run(["sudo", "cp", "-r", "/etc/tor", "."])
#subprocess.run(["sudo", "cp", "-r", "/var/lib/tor", "."])
#os.rename("tor", "TorDomainInfo")

# Download figlet font "Reg.flf"
subprocess.run(["wget", "-O", "~/.local/share/fonts/figlet-fonts/Reg.flf", "https://raw.githubusercontent.com/xero/figlet-fonts/master/ANSI%20Regular.flf"])

# Display success message
print("Installation completed!")
