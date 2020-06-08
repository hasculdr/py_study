#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Задание 19.1

Создать функцию send_show_command.

Функция подключается по SSH (с помощью netmiko) к ОДНОМУ устройству и выполняет указанную команду.

Параметры функции:
* device - словарь с параметрами подключения к устройству
* command - команда, которую надо выполнить

Функция возвращает строку с выводом команды.

Скрипт должен отправлять команду command на все устройства из файла devices.yaml с помощью функции send_show_command.

"""

command = "sh ip int br"
from netmiko import ConnectHandler
import yaml

command = 'sh ip int br'

def send_show_command(device, command): #функции передаются словарь с параметрами подключения к устройству (ip, пароли, тип устройства) и команда в строковый переменной
	print(f'Соединяюсь с устройством {device["host"]}')
	with ConnectHandler(**device) as ssh_session: #открываем ssh-соединение параметры распаковываем из словаря в yaml-файле
		ssh_session.enable() #переход в режим enable
		return(ssh_session.send_command(command)) #возвращаем результат выполнения одной команды
		
if __name__ == "__main__":
	with open('devices.yaml', 'r') as f:
		device_list = yaml.safe_load(f) #считываем содержимое yaml-файла (там список словарей)
	for device in device_list: #для каждого словаря в списке
		print(send_show_command(device, command)) #вызов функции с ssh-подключением


