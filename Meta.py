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

local_port_file = "LPort.io"
if os.path.exists(local_port_file):
    # If it exists, read the local port from it
    with open(local_port_file, "r") as file:
        PORT = file.read().strip()

file_to_delete = "Meta.io" 

if os.path.exists(file_to_delete):
    os.remove(file_to_delete)

while True:
    mac = input("Enter Mac: ")
    option = input("(START/STOP) : ")

    url = 'http://127.0.0.1:5050/Metasploit.php'
    data = {'MAC': mac, 'Option': option}
    response = requests.post(url, data=data)

    if response.status_code == 200:
        print("Data sent successfully.")
    else:
        print("Failed to send data.")
        time.sleep(10)

    file_to_delete = "Meta.io"  

    if os.path.exists(file_to_delete):
     os.remove(file_to_delete)
