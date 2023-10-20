import requests
import time
from termcolor import colored
import os

# Function to read the Tor domain from the file
def read_tor_domain(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        return None

# Read the Tor domain from the file
tor_domain = read_tor_domain('/var/lib/tor/Domain/hostname')

# The URL of the page you want to check
url = f'http://{tor_domain}/WebStatus' if tor_domain else ''

# Tor proxy configuration
proxies = {
    'http': 'socks5h://127.0.0.1:9151',  # Tor proxy address and port for HTTP
    'https': 'socks5h://127.0.0.1:9151'  # Tor proxy address and port for HTTPS
}

# Create a Requests session with proxy configuration
requests_session = requests.Session()
requests_session.proxies.update(proxies)

while True:
    try:
        response = requests_session.get(url)

        if response.status_code == 200:
            status = colored("[+] Connected", 'green')
        else:
            status = colored("[-] Not Connected", 'red')

        response_time = response.elapsed.total_seconds() if response.elapsed else None

        # Page information and response
        os.system("clear")
        os.system("figlet -c -f ~/.local/share/fonts/figlet-fonts/3d.flf WebStatus | lolcat")
        print("=" * 40)
        print(f"Page URL: {url}")
        print(f'Status: {status}')
        if status == colored("[-] Not Connected", 'red'):
            print("Error: Missing dependencies for SOCKS support.")
        elif response_time is not None:
            print(f"Response Time: {response_time:.5f} seconds")
        print("=" * 40)

    except requests.exceptions.RequestException:
        os.system("clear")
        os.system("figlet -c -f ~/.local/share/fonts/figlet-fonts/3d.flf WebStatus | lolcat")
        print("=" * 40)
        print(f"Page URL: {url}")
        print("Status:",colored("[-] Not Connected", 'red'))
        print("Error: Unable to connect to the website.")
        print("=" * 40)

    time.sleep(1)  # Wait for some time before performing a new check
