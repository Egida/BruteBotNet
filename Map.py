import os
import re
import time
import folium
from geopy.geocoders import Nominatim

# Function to clear the terminal screen based on the operating system
def clear_screen():
    if os.name == 'nt':  # Windows
     os.system('cls')
    else:  # Non-Windows (e.g., Linux, macOS)
     os.system('clear')
     os.system("figlet -c -f ~/.local/share/fonts/figlet-fonts/3d.flf IP Map | lolcat")

        
# Directory where the text files are located (replace with your directory pa
directory_path = "."

# Function to extract IP addresses from a text file
def extract_ip_addresses(file_path):
    ip_addresses = []
    with open(file_path, 'r', encoding='latin-1') as file:
        content = file.read()
        # Use a regular expression to find IP addresses in the file
        ip_pattern = r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'
        ip_addresses.extend(re.findall(ip_pattern, content))
    return ip_addresses

# Function to create a map with IP markers using Folium
def create_ip_map(ip_list):
    m = folium.Map(location=[0, 0], zoom_start=2)  # Initial map with a global view

    geolocator = Nominatim(user_agent="ip-geolocator")

    for ip in ip_list:
        location = get_location(ip, geolocator)
        if location:
            folium.Marker(
                location=location,
                popup=f"IP: {ip}",
            ).add_to(m)

    return m

# Function to get location data for an IP address using geopy (Nominatim)
def get_location(ip, geolocator):
    try:
        location = geolocator.geocode(ip)
        if location:
            return [location.latitude, location.longitude]
    except Exception as e:
        print(f"Error: {str(e)}")
        return None

# Main loop to continuously monitor and update the IP map
while True:
    # Initialize a list to store extracted IP addresses
    extracted_ip_addresses = []

    # Process each file in the directory
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        if os.path.isfile(file_path):
            extracted_ip_addresses.extend(extract_ip_addresses(file_path))

    # Create a map with IP markers
    ip_map = create_ip_map(extracted_ip_addresses)

    # Save the map to an HTML file (you can view it in a web browser)
    os.system("rm -rf ip_location_map.html")
    os.system("clear")    
    ip_map.save("ip_location_map.html") 
    os.system("figlet -c -f ~/.local/share/fonts/figlet-fonts/3d.flf IP Map | lolcat")
    print
    print(f"Map saved as 'ip_location_map.html'")
    print("Loading >>>")
    # Wait for five seconds before updating the map again
    time.sleep(1)
