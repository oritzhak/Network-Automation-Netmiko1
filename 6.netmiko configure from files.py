# This script connecting to switches using SSH and writing the configuration in the device from the file configuration.
from netmiko import ConnectHandler

sw1 = { # device details
    'device_type': 'cisco_ios',
    'ip': '192.168.122.72',
    'username': 'david',
    'password': 'cisco'
}

sw2 = {  # device details
    'device_type': 'cisco_ios',
    'ip': '192.168.122.82',
    'username': 'david',
    'password': 'cisco'
}

sw3 = {  # device details
    'device_type': 'cisco_ios',
    'ip': '192.168.122.83',
    'username': 'david',
    'password': 'cisco'
}

all_devices = [sw1, sw2, sw3]  # all device details


with open('access_switch_configuration.txt') as f:
    lines = f.read().splitlines()
print (lines)

all_devices = [sw1, sw2, sw3]  # all device details

for devices in all_devices:
    net_connect = ConnectHandler(**devices) # connect in ssh to the device
    output = net_connect.send_config_set(lines) # implementingthe configurations
    print (output)