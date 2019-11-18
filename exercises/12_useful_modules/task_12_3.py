# -*- coding: utf-8 -*-
'''
Задание 12.3


Создать функцию print_ip_table, которая отображает таблицу доступных и недоступных IP-адресов.

Функция ожидает как аргументы два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Результат работы функции - вывод на стандартный поток вывода таблицы вида:

Reachable    Unreachable
-----------  -------------
10.1.1.1     10.1.1.7
10.1.1.2     10.1.1.8
             10.1.1.9

Функция не должна изменять списки, которые переданы ей как аргументы.
То есть, до выполнения функции и после списки должны выглядеть одинаково.


Для этого задания нет тестов
'''
from tabulate import tabulate
reachable = ['8.8.8.8', '8.8.4.4', '192.168.1.1', '88.147.128.16', '88.147.128.17']
unreachable = ['10.10.10.10', '192.168.0.1']
columns = ['Reachable', 'Unreachable']
def print_ip_table(reachable, unreachable):
	if len(reachable) > len(unreachable):
		dif = int(len(reachable)) - int(len(unreachable))
		while dif != 0:
			unreachable.append('')
			dif -= 1
		return(tabulate(list(zip(reachable, unreachable)), headers = columns, tablefmt = 'pipe'))
	elif len(reachable) < len(unreachable):
		dif = int(len(unreachable)) - int(len(reachable))
		while dif != 0:
			unreachable.append('')
			dif -= 1
		return(tabulate(list(zip(reachable, unreachable)), headers = columns, tablefmt = 'pipe'))
	if len(reachable) == len(unreachable):
		return(tabulate(list(zip(reachable, unreachable)), headers = columns, tablefmt = 'pipe'))
if __name__ == "__main__":
	print(print_ip_table(reachable, unreachable))	
