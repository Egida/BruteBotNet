import requests
import os
import time
from termcolor import *

os.system("clear")
os.system("figlet -c -f ~/.local/share/fonts/figlet-fonts/3d.flf Global | lolcat")
os.system("figlet -c -f ~/.local/share/fonts/figlet-fonts/3d.flf  PShell | lolcat")
print("=" * 40)

while True:
    try:
        if os.path.exists('Data.io'):
            os.remove('Data.io')

        data = input("PowerShell >>> ")
        print("")

        if data.lower() == 'exit':
            break

        response = requests.post(f'http://localhost:8080/Control.php', data={'data': data})
        X = colored(response.text, 'green')
        print(X)
        time.sleep(10)
        if os.path.exists('Data.io'):
            os.remove('Data.io')

    except IndentationError:
        print("IndentationError occurred, skipping...")
        continue

if __name__ == '__main__':
    send_data()
