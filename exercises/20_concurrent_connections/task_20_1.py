# -*- coding: utf-8 -*-
"""
Задание 20.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.
Проверка IP-адресов должна выполняться параллельно в разных потоках.

Параметры функции:
* ip_list - список IP-адресов
* limit - максимальное количество параллельных потоков (по умолчанию 3)

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для выполнения задания можно создавать любые дополнительные функции.

Для проверки доступности IP-адреса, используйте ping.

Подсказка о работе с concurrent.futures:
Если необходимо пинговать несколько IP-адресов в разных потоках,
надо создать функцию, которая будет пинговать один IP-адрес,
а затем запустить эту функцию в разных потоках для разных
IP-адресов с помощью concurrent.futures (это надо сделать в функции ping_ip_addresses).
"""
import subprocess

import yaml
from concurrent.futures import ThreadPoolExecutor, as_completed

def ping(addr):
	reply = subprocess.run(['ping', '-c', '3', '-n', addr], stdout=subprocess.DEVNULL)  # отключаем вывод STDOUT
	if reply.returncode==0:
		return(addr, True)
	else:
		return(addr, False)

		
def ping_ip_addresses(ip_list, limit=3):
	alive=[]
	unreachable=[]
	future_list=[]
	with ThreadPoolExecutor(max_workers=limit) as executor:
		for addr in ip_list:
			future_object=executor.submit(ping, addr)  # передаем методу submit функцию ping и ее аргумент, получаем future-объект
			future_list.append(future_object)  # добавляем этот объект в список
		for future_object in as_completed(future_list):	 # перебираем future-объекты в полученном списке с помощью функции as_completed
			# распаковываем future-объект (ip-адрес, доступен/недоступен),
			# нужно для корректной работы с as_completed, т.к. она не учитывает
			# порядок завершения задач и результат будет "перемешан"
			ip, status = future_object.result()
			if status==True:
				alive.append(ip)
			else:
				unreachable.append(ip)
	return(alive, unreachable)


if __name__=="__main__":
	ip_list=[]
	with open('devices.yaml', 'r') as f:
		device_list=yaml.safe_load(f)
		for device in device_list:
			ip_list.append(device['host'])
		print(ping_ip_addresses(ip_list))


