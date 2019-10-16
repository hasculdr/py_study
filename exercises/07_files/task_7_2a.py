# -*- coding: utf-8 -*-
#!/bin/env python3
'''
Задание 7.2a

Сделать копию скрипта задания 7.2.
​Дополнить скрипт:
  Скрипт не должен выводить команды, в которых содержатся слова,
  которые указаны в списке ignore.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
ignore = ['duplex', 'alias', 'Current configuration']
ignore.append('!')
trash1, trash2, trash3, trash4 = ignore
from sys import argv
data = open(argv[1]).readlines()
for line in data:
	if trash1 in line:
		pass
	elif trash2 in line:
		pass
	elif trash3 in line:
		pass
	elif trash4 in line:
		pass
	else:
		print(line.strip())
