# This script connecting to the switch device using SSH and creating 20 vlans

from netmiko import ConnectHandler
cisco_sw_core = {   # details device
    'device_type': 'cisco_ios',
    'ip': '192.168.122.72',
    'username': 'david',
    'password': 'cisco'
}

net_connect = ConnectHandler(**cisco_sw_core)  # connect ssh to device
output = net_connect.send_command('show ip int brief') # write the command on the switch
print (output) # print the out put

config_commands = ['int loop 0', 'ip address 1.1.1.1 255.255.255.0'] 
output = net_connect.send_config_set(config_commands) # write configuration 
print (output) 

for n in range (2,22):  # create vlan 2-20 with names
    print ("Creating VLAN " + str(n))
    config_commands = ['vlan ' + str(n), 'name Python_VLAN ' + str(n)]
    output = net_connect.send_config_set(config_commands) # create vlan
    print (output) 