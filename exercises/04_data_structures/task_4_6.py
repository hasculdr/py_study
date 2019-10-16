# -*- coding: utf-8 -*-
'''
Задание 4.6

Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
ospf_list = ospf_route.split()
named_list = [['Protocol:', 'OSPF'],
			  ['Prefix:', ospf_list[1]],
			  ['AD/Metric:', ospf_list[2].strip('[]')],
			  ['Next-Hop:', ospf_list[4].strip(',')],
			  ['Last update:', ospf_list[5].strip(',')],
			  ['Outbound Interface:', ospf_list[6]]]
for connection in named_list:
	name, data = connection
	print(f'{name:25} {data:25}')
