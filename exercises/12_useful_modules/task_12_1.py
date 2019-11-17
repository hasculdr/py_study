# -*- coding: utf-8 -*-
'''
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет доступность IP-адресов.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте ping.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
import subprocess
list_addresses = ['8.8.8.8', '88.147.158.9', '10.10.10.10', '192.168.0.4', '0.0.0.0']
def ping_ip_addresses(list_addresses):
	alive = list()
	unreachable = list()
	for address in list_addresses:
		reply = subprocess.run(['ping', '-c', '1', address], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		if reply.returncode == 0:
			alive.append(address)
		else:
			unreachable.append(address)
	output = (alive, unreachable)
	return(output)
if __name__ == "__main__":
	print(ping_ip_addresses(list_addresses))
