import requests
import os
import time

def check_website_status(ports):
    while True:
        os.system("clear")
        os.system(f"figlet -c -f ~/.local/share/fonts/figlet-fonts/3d.flf WebStatus | lolcat")
        # Create website URLs using the extracted or entered ports
        websites = [f"http://bore.pub:{port}/WebStatus" for port in ports]

        for website in websites:
            try:
                response = requests.get(website)
                response.raise_for_status()  # Raise an exception for HTTP errors (4xx and 5xx)
                status = "Connected"
                response_time = response.elapsed.total_seconds()
                status_code = response.status_code
            except requests.exceptions.RequestException as e:
                status = "Not Connected"
                response_time = None
                status_code = None
                error_message = str(e)

            print(f"Website: {website}")
            print(f"Status: {status}")
            if status == "Connected":
                print(f"Response Time: {response_time} seconds")
                print(f"Status Code: {status_code}")
            else:
                print(f"Error Check WebSite!")
            print("=" * 40)

        time.sleep(5)  # Sleep for 60 seconds before the next iteration

def get_ports():
    if os.path.exists("ports.io"):
        with open("ports.io", "r") as file:
            lines = file.readlines()

        ports = []

        for line in lines:
            parts = line.strip().split("=")
            if len(parts) == 2:
                try:
                    port = int(parts[1].strip())
                    ports.append(port)
                except ValueError:
                    print(f"Invalid port value: {parts[1].strip()}")
    else:
        print("No 'ports.io' file found. Please enter 10 ports manually.")
        ports = []
        for i in range(1, 11):
            while True:
                try:
                    port = int(input(f"Your Server Port {i} : "))
                    ports.append(port)
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid integer.")
    return ports

if __name__ == "__main__":
    ports = get_ports()
    check_website_status(ports)
