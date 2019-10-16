# -*- coding: utf-8 -*-
#!/bin/env python3
'''
Задание 7.2c

Переделать скрипт из задания 7.2b:
* передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

Внутри, скрипт должен отфильтровать те строки, в исходном файле конфигурации,
в которых содержатся слова из списка ignore.
И записать остальные строки в итоговый файл.

Проверить работу скрипта на примере файла config_sw1.txt.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

ignore = ['duplex', 'alias', 'Current configuration']
trash1, trash2, trash3 = ignore
from sys import argv
with open(argv[1]) as data, open(argv[2], 'a') as result:
	for line in data.readlines():
		if trash1 in line:
			pass
		elif trash2 in line:
			pass
		elif trash3 in line:
			pass
		else:
			result.writelines(line)
