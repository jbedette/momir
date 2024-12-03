#!/bin/sh

touch ~/Desktop/momir.desktop
chmod +x ~/Desktop/momir.desktop
echo "
[Desktop Entry]
Type=Application
Name=Momir
Exec=python3 ~/momir/pyqt_gui.py
Icon=/usr/share/icons/hicolor/48x48/apps/python3.png
Terminal=true

" >> ~/Desktop/momir.desktop

# sudo apt update && sudo apt upgrade -y
# sudo apt install -y python3 python3-pip python3-dev python3-setuptools libgl1-mesa-dev libgles2-mesa-dev libgstreamer1.0-dev gstreamer1.0-plugins-{bad,base,good,ugly} gstreamer1.0-libav gstreamer1.0-tools libmtdev-dev xclip xsel
# python3 -m pip install --upgrade pip setuptools wheel
# python3 -m pip install cython==0.29.36
# python3 -m pip install kivy[base] kivy[pygame] kivy[angle_sdl2]
# python3 -c "import kivy; print(kivy.__version__)"

