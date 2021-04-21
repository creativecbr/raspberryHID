#!/bin/bash

if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi


current_dir="$(pwd)"

echo "dtoverlay=dwc2" | sudo tee -a /boot/config.txt
echo "dwc2" | sudo tee -a /etc/modules
echo "libcomposite" | sudo tee -a /etc/modules

rm /etc/rc.local
cp "${current_dir}/rc.local" /etc/rc.local
chmod 777 /etc/rc.local

# hid_usb_interface
cp "${current_dir}/isticktoit_usb" /usr/bin/isticktoit_usb
chmod 777 /usr/bin/isticktoit_usb

reboot 
