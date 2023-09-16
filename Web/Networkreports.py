import os
import json
import time

# Function to clear the terminal screen based on the operating system
def clear_screen():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Non-Windows (e.g., Linux, macOS)
        os.system('clear')
        os.system("figlet -c -f ~/.local/share/fonts/figlet-fonts/3d.flf Network | lolcat")
# Directory where the files are located (replace with your directory path)
directory_path = "."

# Function to extract and organize data from a file
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
                
                # Add data to the extracted_data list
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
# Main loop to continuously monitor and update the data
while True:
    # Initialize lists to store extracted data and file details
    extracted_data = []
    file_details = []

    # Clear the terminal screen
    clear_screen()

    # Process each file in the directory
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        if os.path.isfile(file_path):
            extract_and_organize_data(file_path)

    # Display the number of files and extracted data
    num_files = len(file_details)
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
    
    # Wait for a specified interval before scanning again (e.g., 60 seconds)
    time.sleep(1)
