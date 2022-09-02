#!/usr/bin/env bash

function ask() {
    echo $1
    read res
    if [[ $res == 'n' ]]
    then
        return 1
    fi
    return 0
}

function check_and_install_command() {
    which $1 2> /dev/null
    if [[ $? -ne 0 ]]
    then
        ask "$1 is not installed do you want to install it?[Y/n]"
        if [[ $? -ne 0 ]]
        then
            echo "Faild install ziba configuration."
            exit 1
        fi
        echo "Installing $1 ..."
        sudo pacman -S $1

    fi
}

check_and_install_command wget
check_and_install_command unzip

# install dracula gtk theme
ask "Do you want to install dracula gtk them?"

if [[ $? -eq 0 ]]
then
    url=https://github.com/dracula/gtk/archive/master.zip 
    echo "Downloading $url"
    wget -c $url -O /tmp/dracula-gtk-master.zip
    mkdir -p ~/.themes/
    unzip /tmp/dracula-gtk-master.zip -d ~/.themes/
    mv ~/.themes/gtk-master/ ~/.themes/dracula

    # gsettings set org.gnome.desktop.interface gtk-theme "dracula"
    # gsettings set org.gnome.desktop.wm.preferences theme "dracula"
    xfconf-query -c xsettings -p /Net/ThemeName -s "dracula"

    url=https://github.com/dracula/gtk/files/5214870/Dracula.zip
    echo "Downloading $url"
    wget -c $url -O /tmp/dracula-icons-master.zip
    mkdir -p ~/.icons/
    unzip /tmp/dracula-icons-master.zip -d ~/.icons/
    gtk-update-icon-cache ~/.icons/Dracula
    # gsettings set org.gnome.desktop.interface icon-theme "Dracula"
    xfconf-query -c xsettings -p /Net/IconThemeName -s Dracula
fi

# install rofi and rofi dracula theme
ask "Do you want to install rofi?"
if [[ $? -eq 0 ]]
then
    check_and_install_command rofi
    # xfconf-query -c xfce4-keyboard-shortcuts -n -t 'string' -p '/commands/custom/<Super><' -s xfce4-terminal
    xfconf-query --channel xfce4-keyboard-shortcuts --property "/commands/custom/<Super_L><Space>" --create --type string --set "rofi -show drun"
fi
mkdir -p ~/.local/share/Steam/skins/
cd ~/.local/share/Steam/skins/ && git clone https://github.com/dracula/steam.git 'Dracula'

