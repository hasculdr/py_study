# -*- coding: utf-8 -*-
'''
Задание 6.2

1. Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
2. Определить тип IP-адреса.
3. В зависимости от типа адреса, вывести на стандартный поток вывода:
   'unicast' - если первый байт в диапазоне 1-223
   'multicast' - если первый байт в диапазоне 224-239
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
ip = input('Введите IP-адрес в формате A.B.C.D:\n')
octets_list = ip.split('.')
if int(octets_list[0]) >= 1 and int(octets_list[0]) <= 223:
	print('unicast')
elif int(octets_list[0]) >= 224 and int(octets_list[0]) <= 239:
	print('multicast')
elif ip == '255.255.255.255':
	print('local broadcast')
elif ip == '0.0.0.0':
	print('unassigned')
else:
	print('unused')
