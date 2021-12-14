#!/bin/sh
sudo apt update
sudo apt install python3 python3-pip python3-venv -y
python3 -m venv venv
. venv/bin/activate
pip3 install pytest
pip3 install -r requirements.txt

cd Service2
pytest --cov ./application
cd ..
cd Service3
pytest --cov ./application
cd ..
cd Service4
pytest --cov ./application
cd ..