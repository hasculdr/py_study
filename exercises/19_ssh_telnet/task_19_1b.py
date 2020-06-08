# -*- coding: utf-8 -*-
"""
Задание 19.1b

Скопировать функцию send_show_command из задания 19.1a и переделать ее таким образом,
чтобы обрабатывалось не только исключение, которое генерируется
при ошибке аутентификации на устройстве, но и исключение,
которое генерируется, когда IP-адрес устройства недоступен.

При возникновении ошибки, на стандартный поток вывода должно выводиться сообщение исключения.

Для проверки измените IP-адрес на устройстве или в файле devices.yaml.
"""
command = "sh ip int br"
import netmiko
from netmiko import ConnectHandler
import yaml

command = 'sh ip int br'

def send_show_command(device, command): #функции передаются словарь с параметрами подключения к устройству (ip, пароли, тип устройства) и команда в строковый переменной
	try: #ловим исключения
		print(f'Соединяюсь с устройством {device["host"]}')
		with ConnectHandler(**device) as ssh_session: #открываем ssh-соединение параметры распаковываем из словаря в yaml-файле
			ssh_session.enable() #переход в режим enable
			return(ssh_session.send_command(command)) #возвращаем результат выполнения одной команды
	except netmiko.ssh_exception.NetmikoAuthenticationException as err: #вариант для неправильной авторизации на устройстве, описание ошибки сохраняется в переменную err
		print(err)
		#return(err)
	except netmiko.ssh_exception.NetmikoTimeoutException as err: #вариант для недоступного по сети устройства
		print(err)
		#return(err)
		
if __name__ == "__main__":
	with open('devices.yaml', 'r') as f:
		device_list = yaml.safe_load(f) #считываем содержимое yaml-файла (там список словарей)
	for device in device_list: #для каждого словаря в списке
		print(send_show_command(device, command)) #вызов функции с ssh-подключением
