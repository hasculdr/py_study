# -*- coding: utf-8 -*-
'''
Задание 15.4

Создать функцию get_ints_without_description, которая ожидает как аргумент
имя файла, в котором находится конфигурация устройства.


Функция должна обрабатывать конфигурацию и возвращать список имен интерфейсов,
на которых нет описания (команды description).

Пример интерфейса с описанием:
interface Ethernet0/2
 description To P_r9 Ethernet0/2
 ip address 10.0.19.1 255.255.255.0
 mpls traffic-eng tunnels
 ip rsvp bandwidth

Интерфейс без описания:
interface Loopback0
 ip address 10.1.1.1 255.255.255.255

Проверить работу функции на примере файла config_r1.txt.
'''
import re
def get_ints_without_description(config_file):
	regexp = r'\ninterface (\S+)\n (\w+)'
	intf_witgout_descr = []
	with open(config_file, 'r') as config:
		text = config.read()
	matched_values = re.findall(regexp, text)
	for elem in matched_values:
		if 'description' not in elem:
			intf_witgout_descr.append(elem[0])
	return(intf_witgout_descr)
print(get_ints_without_description('config_r1.txt'))
