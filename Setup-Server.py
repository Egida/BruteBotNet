import subprocess
import re
import os
import time
import sys
# Check for root privileges
if os.geteuid() != 0:
    print("You must run the script as a root user or with sudo privileges.")
    sys.exit(1)

# Install necessary packages
packages = ["python3-pip", "python3-socks", "php", "dbus-x11", "gnome-terminal", "lolcat", "figlet", "php-fpm", "nginx"]
subprocess.run(["sudo", "apt", "update"])
subprocess.run(["sudo", "apt", "install"] + packages + ["-y"])

# Install Nginx UI
os.system("bash <(curl -L -s https://raw.githubusercontent.com/0xJacky/nginx-ui/master/install.sh) install")

# Start Nginx and Nginx UI
os.system("systemctl enable nginx")
os.system("systemctl start nginx")
os.system("systemctl enable nginx-ui")
os.system("systemctl start nginx-ui")

# Determine PHP version
php_version_output = subprocess.check_output(['php', '-v'], text=True)
version_match = re.search(r'PHP (\d+\.\d+)', php_version_output)

if version_match:
    major_version = version_match.group(1)
    service_command = f'systemctl enable php{major_version}-fpm'
    service_command = f'systemctl start php{major_version}-fpm'
    subprocess.run(service_command, shell=True)
    print(f'Starting PHP-FPM for PHP version {major_version}.')
else:
    print('Failed to determine PHP version.')
    os.system("apt-get install php php-fpm")
os.system("rm -rf /etc/nginx/sites-available/default")

# Create Nginx configuration
nginx_config = f'''server {{
    listen 8080;
    server_name localhost;
    root {os.getcwd()};
    index index.php index.html index.htm;
    error_log /var/log/nginx/error.log;
    access_log /var/log/nginx/access.log;
    location / {{
        try_files $uri $uri/ =404;
    }}
    location ~ \.php$ {{
        include snippets/fastcgi-php.conf;
        fastcgi_pass unix:/var/run/php/php{major_version}-fpm.sock;
        fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
        include fastcgi_params;
    }}
    location ~ /\.ht {{
        deny all;
    }}
    location ~ [^/]\.php(/|$) {{
        try_files $uri =404;
        fastcgi_pass unix:/var/run/php/php{major_version}-fpm.sock;
        fastcgi_index index.php;
        include fastcgi.conf;
    }}
}}
'''

with open('/etc/nginx/sites-available/default', 'w') as file:
    file.write(nginx_config)

print("Nginx configuration has been saved.")

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
os.system("service tor restart ;systemctl restart tor")
time.sleep(5)

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
if x.lower() == "y":
    os.system("reboot")
else:
    print("You must restart your device to start the services properly. If you previously restarted your device after installing the program, you can continue.")
time.sleep(5)
