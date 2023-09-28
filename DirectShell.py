import requests
import os
import time
from termcolor import colored

# Function to read the port from the LPort.io file
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

    while True:
        data = input("PowerShell >>> ")
        print("")

        if data.lower() == 'exit':
            break

        response = requests.post(f'http://localhost:{port}/Control.php', data={'data': data})

        if response.status_code == 200:
            response_data = response.json()  # Assuming the PHP script returns JSON data
            command_output = response_data.get('command_output', '')
            command_error = response_data.get('command_error', '')

            if command_output:
                print(colored(command_output, 'green'))

            if command_error:
                print(colored(command_error, 'red'))
        else:
            print("Error sending data to the server.")

        time.sleep(10)

if __name__ == '__main__':
    send_data()
