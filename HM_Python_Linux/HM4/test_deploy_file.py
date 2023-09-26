from ssh_helpers import ssh_checkout
from fixtures import prepare
import yaml, pytest

with open('config.yml', 'r') as conf_file:
    config = yaml.safe_load(conf_file)
    
class TestPositive:
    def test_package_installed(self, prepare):    
        assert ssh_checkout(config['ssh_host'],
                 config['ssh_user'],
                 config['ssh_pass'],
                 f"echo '{config['ssh_pass']}' | sudo -S dpkg -s p7zip-full",
                 "Status: install ok installed"
                ) == True
        
class TestNegative:
    def test_package_not_installed(self, prepare):    
        assert ssh_checkout(config['ssh_host'],
                 config['ssh_user'],
                 config['ssh_pass'],
                 f"echo '{config['ssh_pass']}' | sudo -S dpkg -s p7zip-notsofull",
                 "Status: install ok installed"
                ) == False