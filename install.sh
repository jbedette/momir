#!/bin/sh

touch ~/Desktop/momir.desktop
chmod +x ~/Desktop/momir.desktop
echo "
[Desktop Entry]
Type=Application
Name=Momir
Exec=python3 ~/momir/gui.py
Icon=/usr/share/icons/hicolor/48x48/apps/python3.png
Terminal=true

" >> ~/Desktop/momir.desktop

