import requests
import os
import time
from termcolor import colored

os.system("clear")
os.system("figlet -c -f ~/.local/share/fonts/figlet-fonts/3d.flf WebStatus | lolcat")

def safe_input(prompt):
    try:
        return input(prompt)
    except UnicodeDecodeError:
        print("Invalid input. Please enter valid characters.")
        return safe_input(prompt)

def check_bore_status(ports):
    while True:
        os.system("clear")
        os.system("figlet -c -f ~/.local/share/fonts/figlet-fonts/3d.flf WebStatus | lolcat")
        websites = [f"http://bore.pub:{port}/WebStatus" for port in ports]
        check_websites(websites)

def check_serveo_domain_status(domain):
    while True:
        os.system("clear")
        os.system("figlet -c -f ~/.local/share/fonts/figlet-fonts/3d.flf WebStatus | lolcat")
        website = f"https://{domain}.serveo.net/WebStatus"
        check_websites([website])

def check_websites(websites):
    while True:
        for website in websites:
            try:
                response = requests.get(website)
                response.raise_for_status()
                status = colored("[+] Connected", 'green')
                response_time = response.elapsed.total_seconds()
            except requests.exceptions.RequestException as e:
                status = colored("[-] Not Connected", 'red')
                response_time = None

            os.system("clear")
            os.system("figlet -c -f ~/.local/share/fonts/figlet-fonts/3d.flf WebStatus | lolcat")
            print("=" * 40)
            print(f"Website: {website}")
            print(f'Status: {status}')
            if status == colored("[-] Not Connected", 'red'):
                print("Error Check WebSite!")
            elif response_time is not None:
                print(f"Response Time: {response_time:.5f} seconds")
            print("=" * 40)

        time.sleep(5)

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

def get_domain_from_file(file_path):
    try:
        with open(file_path, "r") as file:
            return file.readline().strip()
    except FileNotFoundError:
        return None

def save_domain_to_file(domain, file_path):
    with open(file_path, "w") as file:
        file.write(domain)

while True:
    print("Choose your connectivity service provider:")
    print("1 - BORE")
    print("2 - SERVEO Domain")

    SERVICE = safe_input("Choose (1 or 2): ")

    if SERVICE == "1":
        ports = get_ports_from_file("Ports.io")
        check_bore_status(ports)
    elif SERVICE == "2":
        saved_domain = get_domain_from_file("Domain.io")
        if saved_domain:
            DOMAIN = saved_domain
        else:
            DOMAIN = input("Enter Your Domain: ")
            save_domain_to_file(DOMAIN, "Domain.io")
        check_serveo_domain_status(DOMAIN)
    else:
        print("Invalid choice. Please choose 1 or 2.")
