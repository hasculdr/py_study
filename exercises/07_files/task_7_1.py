# -*- coding: utf-8 -*-
#!/bin/env python3
'''
Задание 7.1

Аналогично заданию 4.6 обработать строки из файла ospf.txt
и вывести информацию по каждой в таком виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
f = open('ospf.txt', 'r')
data = f.readlines()
for elem in data:
	pieces = elem.split()
	print(f'''
	{'Protocol:':25}{'OSPF':25}
	{'Prefix:':25}{pieces[1]:25}
	{'AD/Metric:':25}{pieces[2].strip('[]'):25}
	{'Next-Hop:':25}{pieces[4].strip(','):25}
	{'Last update:':25}{pieces[5].strip(','):25}
	{'Outbound Interface:':25}{pieces[6].strip(','):25}''')
