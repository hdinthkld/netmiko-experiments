import netmiko
from netmiko.exceptions import NetmikoTimeoutException
from unittest.mock import Mock

device = {
    "device_type": "cisco_ios",
    "host": "127.2.0.1",
    "username": "cisco",
    "password": "cisco",
    "port": 22,
    "secret": "cisco"
}

errored = False

netmiko = Mock()

def mock_send_command(command):
    return "cisco IOS 12.2.4"

netmiko.ConnectHandler.return_value.send_command = mock_send_command
netmiko.ConnectHandler.side_effect = netmiko.exceptions.NetmikoTimeoutException("Too slow")
try:
    net_connect = netmiko.ConnectHandler(**device)
except NetmikoTimeoutException as e:
    #print("Connection timed out")
    errored = True
except:
    #print(f"Unknown exception occurred: {e}")
    errored = True

#print(type(net_connect))


if not errored:
    command="show version"
    output = net_connect.send_command(command)
#   print (output)


