# -*- coding: utf-8 -*-
'''
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса. Адрес считается корректно заданным, если он:
   - состоит из 4 чисел разделенных точкой,
   - каждое число в диапазоне от 0 до 255.

Если адрес задан неправильно, выводить сообщение:
'Неправильный IP-адрес'

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
ip = input('Введите IP-адрес в формате A.B.C.D:\n')
octets_list = ip.split('.')
right_nums = list(range(256))
unicast_byte = list(range(1, 224))
multicast_byte = list(range(224, 240))
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
else:
	print('Неправильный IP-адрес')
