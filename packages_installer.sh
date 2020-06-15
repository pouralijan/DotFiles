#!/usr/bin/env bash

if lsb_release -d | grep -qi manjaro
then
    packages_file="packages.txt"
    while IFS= read -r package
    do
        # pacman -Qs "${package}" > /dev/null
        # if [[ $? != 0 ]]

		if ! pacman -Qi "${package}" > /dev/null 2>&1
        then
            echo "Installing ${package}"
            sudo pacman -S "${package}" --noconfirm
        fi
    done < "${packages_file}"
fi
