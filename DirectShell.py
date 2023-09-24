import requests
import os
import time
from termcolor import *
# Function to read the port from the LPort.io file
os.system("clear")
os.system("figlet -c -f ~/.local/share/fonts/figlet-fonts/3d.flf PowerShell | lolcat")
print("=" * 40)
def read_port_from_file():
    if os.path.exists('LPort.io'):
        with open('LPort.io', 'r') as file:
            port = file.read().strip()
            return port
    else:
        print("LPort.io file not found. Please create the file and specify the port.")
        return None

def send_data():
    port = read_port_from_file()

    if port is None:
        return

    if os.path.exists('Data.io'):
        os.remove('Data.io')
    while True:
        data = input("PowerShell >>> ")

        if data.lower() == 'exit':
            break

        response = requests.post(f'http://localhost:{port}/Control.php', data={'data': data})
        X = colored(response.text, 'green')
        print(X)
        time.sleep(10)
        if os.path.exists('Data.io'):
            os.remove('Data.io')

if __name__ == '__main__':
    send_data()
