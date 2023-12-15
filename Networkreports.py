import os
import json
import time

def clear_screen():
    if os.name == 'nt':  
        os.system('cls')
    else:  
        os.system('clear')
        os.system("figlet -c -f ~/.local/share/fonts/figlet-fonts/3d.flf Network | lolcat")

directory_path = "."

def extract_and_organize_data(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        content = file.read()
        try:
            data = json.loads(content)
            if isinstance(data, dict):
                device_id = data.get("DeviceID", "")
                ip_address = data.get("IP_Address", "")
                system = data.get("System", "")
                mac_address = data.get("Mac", "")
                processor = data.get("Processor", "")
                gpu = data.get("GPU", "")
                ram = data.get("Ram", "")
                machine = data.get("Machine", "")
                
                extracted_data.extend([
                    f"---------------------------------------------------------------------------------------",
                    f"DeviceID   : {device_id}",
                    f"IP Address : {ip_address}",
                    f"System     : {system}",
                    f"MAC Address: {mac_address}",
                    f"Processor  : {processor}",
                    f"GPU        : {gpu}",
                    f"RAM        : {ram}",
                    f"Machine    : {machine}",
                    f"---------------------------------------------------------------------------------------",
                ])
                file_details.append(file_path)
            else:
                os.system("")
        except json.JSONDecodeError:
            os.system("")

last_num_files = 0

while True:
    extracted_data = []
    file_details = []

    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        if os.path.isfile(file_path):
            extract_and_organize_data(file_path)

    num_files = len(file_details)

    if num_files != last_num_files:
        clear_screen()

        if num_files > 0:
            print(f"Number of Reports: {num_files}")
            for i, file_path in enumerate(file_details, start=1):
                print(f"Report {i}: {file_path}")
            print("\nTargets Data:")
            for data_row in extracted_data:
                print(data_row)
        else:
            print("---------------------------------------------------------------------------------------")
            print("No Reports with the specified data structure found.")

        last_num_files = num_files

    time.sleep(1)
