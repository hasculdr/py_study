# -*- coding: utf-8 -*-
#!/bin/env python3
'''
Задание 7.2b

Дополнить скрипт из задания 7.2a:
* вместо вывода на стандартный поток вывода,
  скрипт должен записать полученные строки в файл config_sw1_cleared.txt

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore.
Строки, которые начинаются на '!' отфильтровывать не нужно.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ignore = ['duplex', 'alias', 'Current configuration']
trash1, trash2, trash3 = ignore
result = []
from sys import argv
data = open(argv[1]).readlines()
for line in data:
	if trash1 in line:
		pass
	elif trash2 in line:
		pass
	elif trash3 in line:
		pass
	else:
		result.append(line)
output = open('config_sw1_cleared.txt', 'w')
output.writelines(result)
output.close()
