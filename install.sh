#!/bin/sh

touch ~/Desktop/momir.desktop
chmod +x ~/Desktop/momir.desktop
echo "
[Desktop Entry]
Type=Application
Name=Momir
Exec=/usr/bin/python3 ~/momir/pyqt_gui.py > ~/momir_gui.log 2>&1
Path=~/momir
Icon=/usr/share/icons/hicolor/48x48/apps/python3.png
Terminal=false

" >> ~/Desktop/momir.desktop

sudo apt update && sudo apt upgrade -y
sudo apt install -y python3-pip
sudo pip install -y pybluez pyqt5
sudo apt install -y python3-dbus python3-usb
# sudo pip install --upgrade pillow
