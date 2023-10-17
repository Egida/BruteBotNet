#!/bin/bash
cd ~/
if [[ $EUID -ne 0 ]]; then
    echo "This script requires root privileges to execute."
    echo "Please run the script with sudo or as the root user."
    exit 1
fi

mkdir SetupFile
cd SetupFile
sudo apt install python3-pip python3-socks
sudo apt-get update -y
sudo apt-get install python3 python2 python3-pip figlet lolcat git php dbus-x11 gnome-terminal -y

mkdir -p ~/.local/share/fonts/figlet-fonts/
git clone https://github.com/xero/figlet-fonts.git ~/.local/share/fonts/figlet-fonts/
clear
figlet -c -f ~/.local/share/fonts/figlet-fonts/3d.flf Installing... | lolcat
pip install folium geopy psutil wmi Dispatch ping3 termcolor plotly

sudo apt install tor -y
systemctl start tor
service tor start

sudo echo "HiddenServiceDir /var/lib/tor/Domain/
HiddenServicePort 80 127.0.0.1:8080" | sudo tee -a /etc/tor/torrc
echo -e "SocksPort 127.0.0.1:9151" | sudo tee -a /etc/tor/torrc

sleep 5

sudo systemctl restart tor ;sudo service tor restart ;sleep 2 ;sudo cp /var/lib/tor/Domain/hostname . ;sudo cp /etc/tor .;sudo cp /var/lib/tor .;mv tor TorDomainInfo

wget https://github.com/ekzhang/bore/releases/download/v0.5.0/bore-v0.5.0-x86_64-unknown-linux-musl.tar.gz
clear
sleep 1
figlet -c -f ~/.local/share/fonts/figlet-fonts/3d.flf Installing... | lolcat
sudo apt install tar
tar xzvf bore-v0.5.0-x86_64-unknown-linux-musl.tar.gz
rm -rf figlet-fonts bore-v0.5.0-x86_64-unknown-linux-musl.tar.gz
cd ..
mv SetupFile/bore .
mv SetupFile/serveo .
rm -rf SetupFile
wget -O ~/.local/share/fonts/figlet-fonts/Reg.flf https://raw.githubusercontent.com/xero/figlet-fonts/master/ANSI%20Regular.flf
clear
figlet -c -f ~/.local/share/fonts/figlet-fonts/3d.flf Installed! | lolcat
sleep 2
clear
figlet -c -f ~/.local/share/fonts/figlet-fonts/3d.flf Finish! | lolcat
sleep 2
clear
echo Running Service.
sleep 1
clear
echo Running Service..
sleep 1
clear
echo Running Service...
sleep 1
clear
gnome-terminal -- python3 Run-Server.py
exit
