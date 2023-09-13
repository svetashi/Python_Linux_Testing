# Задание 1.
# Условие:
# Написать функцию на Python, которой передаются в качестве параметров команда и текст. 
# Функция должна возвращать True, если команда успешно выполнена и текст найден в её выводе 
# и False в противном случае. Передаваться должна только одна строка, разбиение вывода использовать не нужно.
import subprocess
import pytest          
            
def check_os(command, search_text):
    result = subprocess.run(command , shell=True, stdout=subprocess.PIPE, encoding="utf=8")

    if result.returncode == 0:
        out = result.stdout
        
        if search_text in out:
            return "TRUE"
        else:
            return  "FALSE"
    else:
        return "FALSE"

command_result = check_os("cat /etc/os-release", 'VERSION="22.04.3 LTS (Jammy Jellyfish)"')
print(command_result)
