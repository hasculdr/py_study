# -*- coding: utf-8 -*-
'''
Задание 11.1

Создать функцию parse_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

У функции должен быть один параметр command_output, который ожидает как аргумент вывод команды одной строкой (не имя файла). Для этого надо считать все содержимое файла в строку.

Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:

    {('R4', 'Fa0/1'): ('R5', 'Fa0/1'),
     ('R4', 'Fa0/2'): ('R6', 'Fa0/0')}

В словаре интерфейсы должны быть записаны без пробела между типом и именем. То есть так Fa0/0, а не так Fa 0/0.

Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

def parse_cdp_neighbors(command_output):
	cdp_list_cleared = []
	cdp_list_of_lists = []
	result_dict = {}
	list_for_dict = command_output.split('>')
	dict_key = list_for_dict[0].strip()
	cdp_list = list_for_dict[1].split('\n')
	for elem in cdp_list:
		if '/' in elem:
			cdp_list_cleared.append(elem)
		else:
			continue
	for elem in cdp_list_cleared:
		cdp_list_of_lists.append(elem.split())
	for elem in cdp_list_of_lists:
		key_list = [dict_key, elem[1]+elem[2]]
		value_list = [elem[0], elem[-2]+elem[-1]]
		result_dict[tuple(key_list)] = tuple(value_list)
	return result_dict
if __name__ == "__main__":
	command_output = open('sh_cdp_n_sw1.txt', 'r').read()
	print(parse_cdp_neighbors(command_output))

