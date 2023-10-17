import socket
import mss
import cv2
import numpy as np
from io import BytesIO
import os
os.system("clear")
os.system("figlet -c -f ~/.local/share/fonts/figlet-fonts/3d.flf SCR | lolcat")
os.system("figlet -c -f ~/.local/share/fonts/figlet-fonts/3d.flf Cloning | lolcat")
print("=" * 40)
X = input("LocalHost Port : ")
HOST = '0.0.0.0' 
PORT = int(X)

BPORT = [61723, 3348, 44693, 44688, 12554, 12539, 61956, 12248, 10010, 10012]

for port in BPORT:
    os.system(f"gnome-terminal -- ./bore local {PORT} --to bore.pub -p {port}")

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(0)
print(f"Server is ready to connect on port {PORT}")

client_socket, client_address = server_socket.accept()
print(f"Connected to a client at {client_address}")

with mss.mss() as sct:
    while True:
        screenshot = sct.shot(output='screen.png')

        with open('screen.png', 'rb') as f:
            img_bytes = f.read()

        client_socket.sendall(img_bytes)

        img = cv2.imdecode(np.frombuffer(img_bytes, np.uint8), cv2.IMREAD_COLOR)
        cv2.imshow('Remote Desktop', img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

client_socket.close()
server_socket.close()
cv2.destroyAllWindows()
