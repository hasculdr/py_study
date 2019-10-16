# -*- coding: utf-8 -*-
'''
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт:
Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
input_correct = False
right_nums = list(range(256))
unicast_byte = list(range(1, 224))
multicast_byte = list(range(224, 240))
while not input_correct:
	ip = input('Введите IP-адрес в формате A.B.C.D:\n')
	octets_list = ip.split('.')
	for elem in octets_list:
		try:
			if int(elem) in right_nums:
				check = True
			else:
				check = False
				break
		except ValueError:
			check = False
			break
	size = len(octets_list)
	if size == 4 and check:
		input_correct = True
	else:
		print('Неправильный IP-адрес')
if int(octets_list[0]) in unicast_byte:
	print('unicast')
elif int(octets_list[0]) in multicast_byte:
	print('multicast')
elif ip == '255.255.255.255':
	print('local broadcast')
elif ip == '0.0.0.0':
	print('unassigned')
else:
	print('unused')
