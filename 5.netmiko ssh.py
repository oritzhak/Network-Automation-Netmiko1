# This script connecting to switches using SSH and creating 20 vlans in each device.
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

for devices in all_devices:
    net_connect = ConnectHandler(**devices) #connect in ssh to the device
    for n in range (2,22): # creating vlan 2-21 and name for each device
       print ("Creating VLAN " + str(n))
       config_commands = ['vlan ' + str(n), 'name Python_VLAN ' + str(n)]
       output = net_connect.send_config_set(config_commands)
       print (output)
