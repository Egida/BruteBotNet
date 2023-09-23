import requests
import os
import time
from termcolor import colored

def safe_input(prompt):
    try:
        return input(prompt)
    except UnicodeDecodeError:
        print("Invalid input. Please enter valid characters.")
        return safe_input(prompt)

def check_bore_status(ports):
    while True:
        os.system("clear")
        os.system(f"figlet -c -f ~/.local/share/fonts/figlet-fonts/3d.flf WebStatus | lolcat")
        websites = [f"http://bore.pub:{port}/WebStatus" for port in ports]

        for website in websites:
            try:
                response = requests.get(website)
                response.raise_for_status() 
                status = colored("[+] Connected", 'green')
                response_time = response.elapsed.total_seconds()
                status_code = response.status_code
            except requests.exceptions.RequestException as e:
                status = colored("[-] Not Connected", 'red')
                response_time = None
                status_code = None
                error_message = str(e)

            print("=" * 40)
            print(f"Website: {website}")
            print(f'Status: {status}')
            if status == colored("[+] Connected", 'green'):
                print(f"Response Time: {response_time} seconds")
            else:
                print(f"Error Check WebSite!")
            print("=" * 40)

        time.sleep(5)  
        os.system("clear")

def check_serveo_status(ports):
    while True:
        os.system("clear")
        os.system(f"figlet -c -f ~/.local/share/fonts/figlet-fonts/3d.flf WebStatus | lolcat")
        websites = [f"https://serveo.net:{port}/WebStatus" for port in ports]

        for website in websites:
            try:
                response = requests.get(website)
                response.raise_for_status() 
                status = colored("[+] Connected", 'green')
                response_time = response.elapsed.total_seconds()
                status_code = response.status_code
            except requests.exceptions.RequestException as e:
                status = colored("[-] Not Connected", 'red')
                response_time = None
                status_code = None
                error_message = str(e)

            print("=" * 40)
            print(f"Website: {website}")
            print(f'Status: {status}')
            if status == colored("[+] Connected", 'green'):
                print(f"Response Time: {response_time} seconds")
            else:
                print(f"Error Check WebSite!")
            print("=" * 40)

        time.sleep(5)  
        os.system("clear")

def check_serveo_domain_status(domain):
    while True:
        os.system("clear")
        os.system(f"figlet -c -f ~/.local/share/fonts/figlet-fonts/3d.flf WebStatus | lolcat")
        website = f"https://{domain}.serveo.net/WebStatus"

        try:
            response = requests.get(website)
            response.raise_for_status() 
            status = colored("[+] Connected", 'green')
            response_time = response.elapsed.total_seconds()
            status_code = response.status_code
        except requests.exceptions.RequestException as e:
            status = colored("[-] Not Connected", 'red')
            response_time = None
            status_code = None
            error_message = str(e)

        print("=" * 40)
        print(f"Website: {website}")
        print(f'Status: {status}')
        if status == colored("[+] Connected", 'green'):
            print(f"Response Time: {response_time} seconds")
        else:
            print(f"Error Check WebSite!")
        print("=" * 40)

        time.sleep(5)  
        os.system("clear")

def get_ports_from_file(file_path):
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()

        ports = []
        for line in lines:
            parts = line.strip().split("=")
            if len(parts) == 2:
                try:
                    port = int(parts[1].strip())
                    ports.append(port)
                except ValueError:
                    print(f"Invalid port value: {parts[1].strip()}")

        return ports
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []

print("Choose your connectivity service provider:")
print("1 - BORE")
print("2 - SERVEO")
print("3 - SERVEO Domain")

while True:
    SERVICE = safe_input("Choose (1, 2, or 3): ")
    
    if SERVICE == "1":
        ports = get_ports_from_file("Ports.io")
        check_bore_status(ports)
    elif SERVICE == "2":
        ports = get_ports_from_file("Ports.io")
        check_serveo_status(ports)
    elif SERVICE == "3":
        DOMAIN = input("Enter Your Domain: ")
        check_serveo_domain_status(DOMAIN)
    else:
        print("Invalid choice. Please choose 1, 2, or 3.")
