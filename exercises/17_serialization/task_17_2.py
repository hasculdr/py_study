# -*- coding: utf-8 -*-
'''
Задание 17.2

Создать функцию parse_sh_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

Функция ожидает, как аргумент, вывод команды одной строкой (не имя файла).
Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:
{'R4': {'Fa 0/1': {'R5': 'Fa 0/1'},
        'Fa 0/2': {'R6': 'Fa 0/0'}}}

Интерфейсы должны быть записаны с пробелом. То есть, так Fa 0/0, а не так Fa0/0.


Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt
'''
import re
from pprint import pprint
with open('sh_cdp_n_sw1.txt', 'r') as data:
	show_cdp_neighbors_str = data.read()
def parse_sh_cdp_neighbors(show_cdp_neighbors_str):
	hostname = (re.match(r'.*?(\S+?)>', show_cdp_neighbors_str, re.DOTALL)).group(1)#имя узла, где выполнена show cdp neighbors
	neighbors = (r'(\w+?\d+?)\s+?'#имя соседа Device ID
				 r'(\w+?\s\S+?)\s+?'#порт, на котором сосед найден Local Intrfce
				 r'\d+?\s+?(?:\w\s)+?\s+?\S+?\s+?'#мусор (3-5 колонки)
				 r'(\w+?\s\S+)')#порт соседа Port ID
	match = re.findall(neighbors, show_cdp_neighbors_str, re.DOTALL)
	neighbors_dict = {}#итоговай словарь для функции
	neighbors_subdict = {}#словарь, вложенный в итоговый
	neighbors_dict[hostname] = neighbors_subdict#засовываем в итоговый словарь вложенный 
	for elem in match:
		neighbors_subdict.update({elem[1]: {elem[0]: elem[2]}})#заполняем вложенный словарь по количеству соседей
	return(neighbors_dict)
if __name__ == "__main__":
	pprint(parse_sh_cdp_neighbors(show_cdp_neighbors_str))
