# -*- coding: utf-8 -*-
"""
Задание 20.2

Создать функцию send_show_command_to_devices, которая отправляет
одну и ту же команду show на разные устройства в параллельных потоках,
а затем записывает вывод команд в файл. Вывод с устройств в файле может быть в любом порядке.

Параметры функции:
* devices - список словарей с параметрами подключения к устройствам
* command - команда
* filename - имя файла, в который будут записаны выводы всех команд
* limit - максимальное количество параллельных потоков (по умолчанию 3)

Функция ничего не возвращает.

Вывод команд должен быть записан в файл в таком формате (перед выводом команды надо написать имя хоста и саму команду):

R1#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.1   YES NVRAM  up                    up
Ethernet0/1                192.168.200.1   YES NVRAM  up                    up
R2#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.2   YES NVRAM  up                    up
Ethernet0/1                10.1.1.1        YES NVRAM  administratively down down
R3#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.3   YES NVRAM  up                    up
Ethernet0/1                unassigned      YES NVRAM  administratively down down

Для выполнения задания можно создавать любые дополнительные функции.

Проверить работу функции на устройствах из файла devices.yaml
"""
import yaml
from netmiko import ConnectHandler
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime

def send_show_command(device, command):
	with ConnectHandler(**device) as ssh_session: #открываем ssh-соединение параметры распаковываем из словаря в yaml-файле
		ssh_session.enable() #переход в режим enable
		prompt=ssh_session.find_prompt()  # определяем и сохраняем приглашение командной строки
		result=ssh_session.send_command(command)  #сохраняем выполнение команды
		return(prompt+command+'\n', result+'\n') #возвращаем имя хоста и команду, символы переноса строки - костыль


def send_show_command_to_devices(devices, command, filename, limit=3):
	with ThreadPoolExecutor(max_workers=limit) as executor:
		future_list=[]
		for device in devices:	
			future_object=executor.submit(send_show_command, device, command)
			future_list.append(future_object)
	with open(filename, 'w') as o_f:
		for future_object in as_completed(future_list):
			o_f.writelines(future_object.result())


if __name__=="__main__":
	start_time=datetime.now()
	command='sh ip int br'
	filename='task_20_2_output.txt'
	with open('devices.yaml','r') as i_f:
		devices=yaml.safe_load(i_f)
		for device in devices:
			send_show_command_to_devices(devices, command, filename)
	print(datetime.now()-start_time)
