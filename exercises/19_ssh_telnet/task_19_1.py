# -*- coding: utf-8 -*-
'''
Задание 19.1

Создать функцию send_show_command.

Функция подключается по SSH (с помощью netmiko) к одному устройству и выполняет указанную команду.

Параметры функции:
* device - словарь с параметрами подключения к устройству
* command - команда, которую надо выполнить

Функция возвращает строку с выводом команды.

Скрипт должен отправлять команду command на все устройства из файла devices.yaml с помощью функции send_show_command.

'''
from netmiko import ConnectHandler
import yaml

command = 'sh ip int br'

def send_show_command(device, command):
	print(f'Соединяюсь с устройством {device["ip"]}')
	with ConnectHandler(**device) as ssh_session:
		ssh_session.enable()
		return(ssh_session.send_command(command))
		
if __name__ == "__main__":
	with open('devices.yaml', 'r') as f:
		device_list = yaml.safe_load(f)
	for device in device_list:
		print(send_show_command(device, command))


