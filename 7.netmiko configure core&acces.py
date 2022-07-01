# This script connecting to switches using SSH and writing the configuration in the device from the file configuration.
from netmiko import ConnectHandler

iosv_l2_s2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.82',
    'username': 'david',
    'password': 'cisco',
}

iosv_l2_s3 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.83',
    'username': 'david',
    'password': 'cisco',
}

iosv_l2_s4 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.84',
    'username': 'david',
    'password': 'cisco',
}

iosv_l2_s5 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.85',
    'username': 'david',
    'password': 'cisco',
}

iosv_l2_s6 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.86',
    'username': 'david',
    'password': 'cisco',
}

with open('access_switch_configuration.txt') as f:
    lines = f.read().splitlines()
print (lines)


access_switches = [iosv_l2_s4, iosv_l2_s5, iosv_l2_s6]

for access_switch in access_switches:
    net_connect = ConnectHandler(**access_switch)
    output = net_connect.send_config_set(lines)
    print (output)


with open('core_switch_configuration.txt') as f:
    lines = f.read().splitlines()
print (lines)


core_switches = [iosv_l2_s4, iosv_l2_s3, iosv_l2_s2]

for core_switch in core_switches:
    net_connect = ConnectHandler(**core_switch )
    output = net_connect.send_config_set(lines)
    print (output)
