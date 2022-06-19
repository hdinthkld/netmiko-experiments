import unittest
import logging
from unittest.mock import patch
from CiscoIosDeviceBackup import Device as CiscoIosDevice

class TestCiscoIosBasicConnection(unittest.TestCase):
    logging.basicConfig(
        level=logging.DEBUG,
        filename="test.log",
        filemode="w",
        encoding="utf-8",
        format="%(asctime)s %(levelname)s:%(module)s.%(funcName)s:%(lineno)d %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    
    @patch.object(CiscoIosDevice,"connect",return_value = None)
    def test_basic_connection(self, mock_connect):
        username = "cisco"
        password= "cisco"
        host_ip = "127.255.255.255"
        device = CiscoIosDevice()

        device.connect(host_ip,username,password)
            
    @patch.object(CiscoIosDevice,"get_config")
    def test_get_config(self,mock_get_config):
        mock_config="Version 15.1\nhostname MOCK-RTR01-SITE01"
        mock_get_config.return_value = mock_config
        device = CiscoIosDevice()

        with patch.object(CiscoIosDevice, "get_config", return_value=mock_config) as mock_get_config:
            config = device.get_config()
            logging.info(f"Got Config")
            config_lines = config.split("\n")
            
            logging.debug("Full Obtained config below:")
            for line in config_lines:
                logging.debug(f"\t{line}")

            self.assertIn("Version 15.1",config.split("\n"),msg="Did not receive expected config")

