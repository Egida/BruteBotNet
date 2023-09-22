import os
import re
import time
import folium
from geopy.geocoders import Nominatim

def clear_screen():
    if os.name == 'nt':  
     os.system('cls')
    else:  
     os.system('clear')
     os.system("figlet -c -f ~/.local/share/fonts/figlet-fonts/3d.flf IP Map | lolcat")

        
directory_path = "."

def extract_ip_addresses(file_path):
    ip_addresses = []
    with open(file_path, 'r', encoding='latin-1') as file:
        content = file.read()
        ip_pattern = r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'
        ip_addresses.extend(re.findall(ip_pattern, content))
    return ip_addresses

def create_ip_map(ip_list):
    m = folium.Map(location=[0, 0], zoom_start=2)  
    geolocator = Nominatim(user_agent="ip-geolocator")

    for ip in ip_list:
        location = get_location(ip, geolocator)
        if location:
            folium.Marker(
                location=location,
                popup=f"IP: {ip}",
            ).add_to(m)

    return m

def get_location(ip, geolocator):
    try:
        location = geolocator.geocode(ip)
        if location:
            return [location.latitude, location.longitude]
    except Exception as e:
        print(f"Error: {str(e)}")
        return None

while True:
    extracted_ip_addresses = []

    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        if os.path.isfile(file_path):
            extracted_ip_addresses.extend(extract_ip_addresses(file_path))

    ip_map = create_ip_map(extracted_ip_addresses)

    os.system("rm -rf ip_location_map.html")
    os.system("clear")    
    ip_map.save("ip_location_map.html") 
    os.system("figlet -c -f ~/.local/share/fonts/figlet-fonts/3d.flf IP Map | lolcat")
    print
    print(f"Map saved as 'ip_location_map.html'")
    print("Loading >>>")
    time.sleep(1)
