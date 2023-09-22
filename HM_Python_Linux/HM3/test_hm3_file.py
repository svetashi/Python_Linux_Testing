from checkout_script import checkout
from fixtures import make_folders, make_files, make_string
import pytest
import yaml

with open("config.yaml") as f:
    data = yaml.safe_load(f.read())

class TestPositive:
    def test_step1(self,make_folders, make_files, make_string):
        assert checkout(f"cd {data['folderin']};7z a {data['folderout']}/arch1", "Everything is Ok"), "test_step1 FAIL"

    # def test_step2():
    #     assert checkout(f"7z d {data['folderout']}/arch1.7z" , "Everything is Ok"), "test_step2 FAIL" 

    # def test_step3():
    #     assert checkout(f"cd {data['folderext']}; 7z u {data['folderout']}/arch1.7z", "Everything is Ok") , "test_step3 FAIL" 
        
    # def test_step4():
    #     assert checkout(f"7z l {data['folderout']}/arch1.7z", "2 files") , "test_step3 FAIL" 
        
    # def test_step5():
    #     assert checkout(f"cd {data['folderext']}; 7z x {data['folderout']}/arch1.7z -y", "Everything is Ok") , "test_step3 FAIL" 

    # def test_step6():
    #     assert checkout(f"crc32 {data['folderout']}/arch1.7z", "a304c2a6") , "test_step3 FAIL" 

if __name__ == "__main__":
    pytest.main(["-vv"])