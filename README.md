[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-370/)
[![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-380/)
[![Python 3.9](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/release/python-390/)
[![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

# Network-Automation-BackUp-System with Nornir, NetBox

It is a tool for changing or backing up configuration on network devices.<br/>
It receives network data devices from Netbox using Nornir with
nornir_netbox plugin.

**IMPORTANT: READ INSTRUCTIONS CAREFULLY BEFORE RUNNING THIS PROGRAM**


## Requirements
### Software
* python >= 3.8
* nornir
* napalm
* napalm-ce
* napalm-eltex
* nornir-napalm
* nornir-netbox
* nornir-utils
* paramiko
* netmiko
* Flask

### Environment
* NetBox >= 3.0
### Device vendors
* Cisco
* Huawei
* Eltex
* If you need another device, then install an additional plugin for NAPALM

# Installing

## Ubuntu 18.04 & 20.04
```
sudo apt-get update && sudo apt-get install python3-venv
```

## Clone repo and install dependencies
* download and setup of virtual environment
```
cd /opt
git clone https://github.com/Sivolen/Network-Automation-tools
cd netbox_confog_backup-sync
python3 -m venv .venv
. .venv/bin/activate
pip3 install -r requirements.txt || pip install -r requirements.txt
```

# Running the script
```
Coming soon
```

## Setup
Copy the [config_example.py](config_example.py) sample settings file to `config.py`.<br/>
Copy the [config_example.yaml](config_example.yaml) sample settings file to `config.yaml`.<br/>
If you are not using NetBox, then edit the [config_example.yaml](config_example.yaml) according to the [documentation](https://nornir.readthedocs.io/en/latest/tutorial/initializing_nornir.html). </br>
All options are described in the example file.

## Thanks
Nornir and nornir_netbox teams

