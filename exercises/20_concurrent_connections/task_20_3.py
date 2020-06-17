# -*- coding: utf-8 -*-
"""
Задание 20.3

Создать функцию send_command_to_devices, которая отправляет
разные команды show на разные устройства в параллельных потоках,
а затем записывает вывод команд в файл. Вывод с устройств в файле может быть в любом порядке.

Параметры функции:
* devices - список словарей с параметрами подключения к устройствам
* commands_dict - словарь в котором указано на какое устройство отправлять какую команду. Пример словаря - commands
* filename - имя файла, в который будут записаны выводы всех команд
* limit - максимальное количество параллельных потоков (по умолчанию 3)

Функция ничего не возвращает.

Вывод команд должен быть записан в файл в таком формате (перед выводом команды надо написать имя хоста и саму команду):

R1#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.1   YES NVRAM  up                    up
Ethernet0/1                192.168.200.1   YES NVRAM  up                    up
R2#sh int desc
Interface                      Status         Protocol Description
Et0/0                          up             up
Et0/1                          up             up
Et0/2                          admin down     down
Et0/3                          admin down     down
Lo9                            up             up
Lo19                           up             up
R3#sh run | s ^router ospf
router ospf 1
 network 0.0.0.0 255.255.255.255 area 0


Для выполнения задания можно создавать любые дополнительные функции.

Проверить работу функции на устройствах из файла devices.yaml и словаре commands
"""
import yaml
from netmiko import ConnectHandler
from concurrent.futures import ThreadPoolExecutor, as_completed

def send_show_command(device, command):
	with ConnectHandler(**device) as ssh_session:
		ssh_session.enable()
		prompt=ssh_session.find_prompt()
		run_show_command=ssh_session.send_command(command)
		result=(prompt+command+'\n', run_show_command+'\n')
	return(result)
	

def send_command_to_devices(devices, commands_dict, filename, limit=3):
	with ThreadPoolExecutor(max_workers=limit) as executor:
		future_list=[]
		for device in devices:
			ip=device['host']  #получаем ip-адрес из словаря для подключений
			command=commands_dict[ip]  #используем его как ключ для словаря с командами, получаем оттуда соответствующую команду
			future_object=executor.submit(send_show_command, device, command)  #передаем функцию,ключ пары (ip-адрес), значение пары (команда)
			future_list.append(future_object)
		with open(filename, 'w') as f:
			for future_object in as_completed(future_list):
				f.writelines(future_object.result())
	return(None)
			
			
commands = {"192.168.100.3": "sh run | s ^router ospf",
			"192.168.100.1": "sh ip int br",
			"192.168.100.2": "sh int desc"}

filename='task_20_3_output.txt'


if __name__=="__main__":
	with open('devices.yaml', 'r') as f:
		devices=yaml.safe_load(f)
		send_command_to_devices(devices, commands, filename)
