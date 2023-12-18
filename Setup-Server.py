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
subprocess.run(["bash", "-c", "curl -L -s https://raw.githubusercontent.com/0xJacky/nginx-ui/master/install.sh | bash -s install"])

# Start Nginx and Nginx UI
subprocess.run(["sudo", "systemctl", "enable", "nginx"])
subprocess.run(["sudo", "systemctl", "start", "nginx"])
subprocess.run(["sudo", "systemctl", "enable", "nginx-ui"])
subprocess.run(["sudo", "systemctl", "start", "nginx-ui"])

# Determine PHP version
try:
    php_version_output = subprocess.check_output(['php', '-v'], text=True)
    version_match = re.search(r'PHP (\d+\.\d+)', php_version_output)

    if version_match:
        major_version = version_match.group(1)
        subprocess.run(["sudo", "systemctl", "enable", f"php{major_version}-fpm"])
        subprocess.run(["sudo", "systemctl", "start", f"php{major_version}-fpm"])
        print(f'Starting PHP-FPM for PHP version {major_version}.')
    else:
        print('Failed to determine PHP version.')
        subprocess.run(["sudo", "apt-get", "install", "php", "php-fpm"])
except subprocess.CalledProcessError:
    print("PHP is not installed. Please install PHP and run the script again.")

# Remove default Nginx configuration
subprocess.run(["sudo", "rm", "-rf", "/etc/nginx/sites-available/default"])

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

def print_and_reduce_path():
    current_path = os.popen("pwd").read().strip()
    print("Current Path:", current_path)

    printed_paths = set()

    while os.path.dirname(current_path) != current_path and len(printed_paths) < 2:
        new_path = os.path.dirname(current_path)
        if new_path != current_path and new_path not in printed_paths:
            printed_paths.add(new_path)
        current_path = new_path

    if len(printed_paths) == 2:
        sorted_paths = sorted(printed_paths, key=len, reverse=True)
        for path in sorted_paths:
            os.system(f"sudo chmod 755 {path}")
            os.system(f"sudo chown -R www-data:www-data {path}")
            print(f"Done chmod/chown! >>> {path}")
            print("Reduced Path:", path)

if __name__ == "__main__":
    print_and_reduce_path()
    
# Restart Nginx
subprocess.run("sudo systemctl restart nginx", shell=True, check=True)

# Clone figlet fonts
figlet_fonts_path = "/root/.local/share/fonts/figlet-fonts/"
os.makedirs(figlet_fonts_path, exist_ok=True)
subprocess.run(["git", "clone", "https://github.com/xero/figlet-fonts.git", figlet_fonts_path])
subprocess.run(["mv", os.path.join(figlet_fonts_path, 'ANSI Regular.flf'), os.path.join(figlet_fonts_path, '3d.flf')])

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
torrc_path = "/etc/tor/torrc"
with open(torrc_path, "a") as torrc:
    torrc.write(tor_config)
subprocess.run(["sudo", "service", "tor", "restart"])
subprocess.run(["sudo", "systemctl", "restart", "tor"])
time.sleep(5)

# Download figlet font "3d.flf"
subprocess.run(["wget", "-O", os.path.join(figlet_fonts_path, '3d.flf'), "https://raw.githubusercontent.com/xero/figlet-fonts/master/ANSI%20Regular.flf"])

# Display success message
print("Installation completed!")
subprocess.run(["clear"])
os.system("figlet -c -f /root/.local/share/fonts/figlet-fonts/3d.flf Restart? | lolcat")
print("Operating instructions : ")

print("=" * 40)
print("You must restart your device to start the services properly. Do you want to restart your device now? (y/n)")
print("=" * 40)
print('->>> Run "python3 Run-Server.py" to start service (after restart).')
print("=" * 40)
x = input(" >>> ")
if x.lower() == "y":
    subprocess.run(["sudo", "reboot"])
else:
    print("You must restart your device to start the services properly. If you previously restarted your device after installing the program, you can continue.")
time.sleep(5)
