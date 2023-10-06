import os
import requests
import time
from termcolor import colored

possible_paths = [
    "/var/lib/tor/Domain/hostname",
    "~/hostname",
    "~/TorDomainInfo/Domain/hostname",
]

def find_tor_host_file():
    for path in possible_paths:
        expanded_path = os.path.expanduser(path)
        if os.path.isfile(expanded_path):
            return expanded_path
    return None

def read_tor_domain(file_path):
    try:
        with open(file_path, "r") as file:
            return file.readline().strip()
    except FileNotFoundError:
        return None

def check_tor_domain_status(tor_domain):
    while True:
        try:
            tor_address = f"http://{tor_domain}/WebStatus"

            response = requests.get(tor_address)
            response.raise_for_status()
            status = colored("[+] Connected", 'green')
            response_time = response.elapsed.total_seconds()
        except requests.exceptions.RequestException as e:
            status = colored("[-] Not Connected", 'red')
            response_time = None

        os.system("clear")
        os.system("figlet -c -f ~/.local/share/fonts/figlet-fonts/3d.flf WebStatus | lolcat")
        print("=" * 40)
        print(f"Tor Domain: {tor_domain}")
        print(f'Status: {status}')
        if status == colored("[-] Not Connected", 'red'):
            print("Error Checking Tor Domain!")
        elif response_time is not None:
            print(f"Response Time: {response_time:.5f} seconds")
        print("=" * 40)

        time.sleep(5)

tor_host_file = find_tor_host_file()
if tor_host_file:
    tor_domain = read_tor_domain(tor_host_file)
    if tor_domain:
        check_tor_domain_status(tor_domain)
    else:
        print(f"Tor domain not found in {tor_host_file}")
else:
    print("Tor host file not found in any of the specified paths.")
