# -*- coding: utf-8 -*-
'''
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Дополнить скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
user_input = input('Введите номер VLAN: ')
data = (open('CAM_table.txt').readlines())
new_list = []
for line in data:
	if '.' in line:
		new_list.append(line.split())
for elem in new_list:
	vlan, mac, _, port = elem
	if user_input == vlan:
		print((f'{vlan:<8}{mac:18}{port:6}'))
