#!/bin/sh
sudo -s
apt update
apt -y install python3
apt -y install wine
python3 main.py
