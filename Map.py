import os
import re
import time
import folium
import requests

m = folium.Map()

search_dir = "."

file_pattern = r".*\.txt"  # يمكنك تغيير النمط حسب احتياجاتك

while True:
    m = folium.Map()  
    for root, dirs, files in os.walk(search_dir):
        for filename in files:
            if re.match(file_pattern, filename):
                with open(os.path.join(root, filename), 'r') as file:
                    data = file.read()
                    ip_address = re.search(r'"IP_Address": "(\d+\.\d+\.\d+\.\d+)"', data)
                    if ip_address:
                        ip_address = ip_address.group(1)
                        response = requests.get(f"https://api.ipfind.com?ip={ip_address}")
                        if response.status_code == 200:
                            location_data = response.json()
                            latitude = location_data.get("latitude")
                            longitude = location_data.get("longitude")
                            folium.Marker([float(latitude), float(longitude)], popup=data).add_to(m)
                        else:
                            print(f"Unable to find coordinates for IP address: {ip_address}")

    m.save('map.html')

    os.system("clear")
    os.system("figlet -c -f ~/.local/share/fonts/figlet-fonts/3d.flf IP Map | lolcat")
    time.sleep(60)
    os.system("rm -rf ip_location_map.html")  # Remove existing file

