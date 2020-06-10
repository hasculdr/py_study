# -*- coding: utf-8 -*-
"""
Задание 19.2c

Скопировать функцию send_config_commands из задания 19.2b и переделать ее таким образом:

Если при выполнении команды возникла ошибка,
спросить пользователя надо ли выполнять остальные команды.

Варианты ответа [y]/n:
* y - выполнять остальные команды. Это значение по умолчанию, поэтому нажатие любой комбинации воспринимается как y
* n или no - не выполнять остальные команды

Функция send_config_commands по-прежнему должна возвращать кортеж из двух словарей:
* первый словарь с выводом команд, которые выполнились без ошибки
* второй словарь с выводом команд, которые выполнились с ошибками

Оба словаря в формате
* ключ - команда
* значение - вывод с выполнением команд

Проверить работу функции можно на одном устройстве.

Пример работы функции:

In [11]: result = send_config_commands(r1, commands)
Подключаюсь к 192.168.100.1...
Команда "logging 0255.255.1" выполнилась с ошибкой "Invalid input detected at '^' marker." на устройстве 192.168.100.1
Продолжать выполнять команды? [y]/n: y
Команда "logging" выполнилась с ошибкой "Incomplete command." на устройстве 192.168.100.1
Продолжать выполнять команды? [y]/n: n

In [12]: pprint(result)
({},
 {'logging': 'config term\n'
             'Enter configuration commands, one per line.  End with CNTL/Z.\n'
             'R1(config)#logging\n'
             '% Incomplete command.\n'
             '\n'
             'R1(config)#',
  'logging 0255.255.1': 'config term\n'
                        'Enter configuration commands, one per line.  End with '
                        'CNTL/Z.\n'
                        'R1(config)#logging 0255.255.1\n'
                        '                   ^\n'
                        "% Invalid input detected at '^' marker.\n"
                        '\n'
                        'R1(config)#'})

"""

# списки команд с ошибками и без:
commands_with_errors = ["logging 0255.255.1", "logging", "a"]
correct_commands = ["logging buffered 20010", "ip http server"]

commands = commands_with_errors + correct_commands

import yaml
from netmiko import ConnectHandler
from pprint import pprint
import re

def send_config_commands(device, config_commands, log=True):
	error_commands=dict()
	normal_commands=dict()
	if log==True:
		print(f'Соединяюсь с устройством {device["host"]}...')
	with ConnectHandler (**device) as ssh_session:
			ssh_session.enable()
			for command in config_commands:
				result = ssh_session.send_config_set(command) #сохраняем вывод команды для анализа
				err = re.search(r'(%.*)\n', result) #анализируем, перенос строки \n не сохраняется при нахождении совпадений
				if err == None: #если совпадений не найдено
					normal_commands[command] = result #команда записывается в словарь_без_ошибок
				else: #если совпадение есть
					print(f'Команда \"{command}\" выполнилась с ошибкой \"{err.group(1)}\" на устройстве {device["host"]}')
					choise = input('Продолжать выполнять команды? [y]/n: ')
					if 'n' in choise or 'no' in choise:
						error_commands[command] = result #команда записывается в словарь_с_ошибками
						break
					else:
						error_commands[command] = result #команда записывается в словарь_с_ошибками
	return(normal_commands, error_commands)
		
if __name__ == "__main__":
	with open('devices.yaml', 'r') as f:
		device_list = yaml.safe_load(f)
		for device in device_list:
			pprint(send_config_commands(device, commands))
