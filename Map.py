import os
import re
import time
import requests
import plotly.graph_objects as go
 

os.system("clear")
os.system("figlet -c -f ~/.local/share/fonts/figlet-fonts/3d.flf IP Map | lolcat")

# Replace with your preferred geocoding service (e.g., GeoIP2, ipinfo.io)
GEOCODING_SERVICE_URL = "https://ipinfo.io"
HTML_FILE_NAME = "ip_globe.html"
UPDATE_INTERVAL_SECONDS = 5  # Update the globe every 5 minutes

def delete_existing_html_file():
    if os.path.exists(HTML_FILE_NAME):
        os.remove(HTML_FILE_NAME)

def extract_ip_addresses(file_path):
    ip_addresses = []
    with open(file_path, 'r', encoding='latin-1') as file:
        content = file.read()
        ip_pattern = r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'
        ip_addresses.extend(re.findall(ip_pattern, content))
    return ip_addresses

def get_location(ip):
    response = requests.get(f"{GEOCODING_SERVICE_URL}/{ip}/json")
    if response.status_code == 200:
        data = response.json()
        if 'loc' in data:
            lat, lon = data['loc'].split(',')
            return float(lat), float(lon)
    return None

def create_ip_globe(ip_list):
    fig = go.Figure()

    # Add a scatter plot of IP addresses
    for ip_info in ip_list:
        location = get_location(ip_info)
        if location:
            lat, lon = location
            fig.add_trace(
                go.Scattergeo(
                    lon=[lon],
                    lat=[lat],
                    hovertext=[f"IP: {ip_info}"],
                    mode="markers",
                    marker=dict(size=8, color="red"),
                )
            )

    # Customize the layout of the globe
    fig.update_geos(
        projection_type="orthographic",
        showland=True,
        landcolor="rgb(243, 243, 243)",
        countrycolor="rgb(204, 204, 204)",
    )

    # Set the layout of the figure
    fig.update_layout(
        title="IP Addresses on the Globe",
        geo=dict(
            showcoastlines=True,
        ),
    )

    # Save the figure as an HTML file
    fig.write_html(HTML_FILE_NAME)

# Delete the existing HTML file (if any)
delete_existing_html_file()

while True:
    extracted_ip_addresses = []

    for filename in os.listdir():
        if os.path.isfile(filename):
            extracted_ip_addresses.extend(extract_ip_addresses(filename))

    create_ip_globe(extracted_ip_addresses)

    print()
    print(f"Globe updated and saved as '{HTML_FILE_NAME}'. Waiting for the next update...")
    time.sleep(UPDATE_INTERVAL_SECONDS)
