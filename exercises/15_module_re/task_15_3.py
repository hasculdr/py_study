# -*- coding: utf-8 -*-
'''
Задание 15.3

Создать функцию convert_ios_nat_to_asa, которая конвертирует правила NAT из синтаксиса cisco IOS в cisco ASA.

Функция ожидает такие аргументы:
- имя файла, в котором находится правила NAT Cisco IOS
- имя файла, в который надо записать полученные правила NAT для ASA

Функция ничего не возвращает.

Проверить функцию на файле cisco_nat_config.txt.

Пример правил NAT cisco IOS
ip nat inside source static tcp 10.1.2.84 22 interface GigabitEthernet0/1 20022
ip nat inside source static tcp 10.1.9.5 22 interface GigabitEthernet0/1 20023

И соответствующие правила NAT для ASA:
object network LOCAL_10.1.2.84
 host 10.1.2.84
 nat (inside,outside) static interface service tcp 22 20022
object network LOCAL_10.1.9.5
 host 10.1.9.5
 nat (inside,outside) static interface service tcp 22 20023

В файле с правилами для ASA:
- не должно быть пустых строк между правилами
- перед строками "object network" не должны быть пробелы
- перед остальными строками должен быть один пробел

Во всех правилах для ASA интерфейсы будут одинаковыми (inside,outside).
'''
import re
def convert_ios_nat_to_asa(nat, asa):
	#			  nat  inside       static tcp			ip			 port1         port2
	regex = r'ip (\w+) (\w+) source (\w+) (\w+) (\d+\.\d+\.\d+\.\d+) (\d+) \S+ \S+ (\d+)'
	values = []
	with open(nat, 'r') as nat_list:
		ios_rules = nat_list.read()
	values = (re.findall(regex, ios_rules))
	with open(asa, 'w') as asa_list:
		for elem in values:
			asa_list.write(f'object network LOCAL_{elem[4]}\n host {elem[4]}\n {elem[0]} (inside,outside) {elem[2]} interface service {elem[3]} {elem[5]} {elem[6]}\n')
print(convert_ios_nat_to_asa('cisco_nat_config.txt', '15_3_output.txt'))
	
	
