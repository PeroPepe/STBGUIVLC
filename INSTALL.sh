curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt install -y nodejs
npm install -g electron
mkdir vlc-stb-electron && cd vlc-stb-electron
npm init -y
npm install electron axios
