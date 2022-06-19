import netmiko

class Device:
    DEFAULT_SSH_PORT = 22
    DEFAULT_SOFTWARE_PLATFORM = "cisco_ios"
    DEFAULT_CONFIG_COMMAND = "show running-config"

    def __init__(self):
        self.connection = None

    def connect(self, ip: str, username: str, password: str, 
                hostname: str = None, secret: str = None, 
                verify_hostname: bool = False, ssh_port: int =  DEFAULT_SSH_PORT):

        connection_config = {
            "device_type": Device.DEFAULT_SOFTWARE_PLATFORM,
            "host": ip,
            "username": username,
            "password": password,
            "port": ssh_port,
            "secret": password if secret is None else secret
}

        self.connection = netmiko.ConnectHandler(**connection_config)
        try:
            self.connection = netmiko.ConnectHandler(**connection_config)
        except:
            raise

    def disconnect(self):
        pass

    def get_config(self, alt_config_command: str = None):
        command= self.DEFAULT_CONFIG_COMMAND if alt_config_command is None else alt_config_command
        output = self.connection.send_command(command)
        return output
