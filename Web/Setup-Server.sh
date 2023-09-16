mkdir SetupFile
cd SetupFile
sudo apt-get update -y
sudo apt-get install python3 python2 python3-pip figlet lolcat git php -y
mkdir -p ~/.local/share/fonts/figlet-fonts/
git clone https://github.com/xero/figlet-fonts.git ~/.local/share/fonts/figlet-fonts/
clear
figlet -c -f ~/.local/share/fonts/figlet-fonts/3d.flf Installing... | lolcat
pip install folium geopy
wget https://github.com/ekzhang/bore/releases/download/v0.5.0/bore-v0.5.0-x86_64-unknown-linux-musl.tar.gz
clear
sleep 1
figlet -c -f ~/.local/share/fonts/figlet-fonts/3d.flf Installing... | lolcat
sudo apt install tar
tar xzvf bore-v0.5.0-x86_64-unknown-linux-musl.tar.gz
rm -rf figlet-fonts bore-v0.5.0-x86_64-unknown-linux-musl.tar.gz
clear
figlet -c -f ~/.local/share/fonts/figlet-fonts/3d.flf Installed! | lolcat
sleep 2
clear
figlet -c -f ~/.local/share/fonts/figlet-fonts/3d.flf Running! | lolcat
cd ..
python3 Run-Server.py
