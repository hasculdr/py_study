# -*- coding: utf-8 -*-
'''
Задание 17.1

В этом задании нужно:
* взять содержимое нескольких файлов с выводом команды sh version
* распарсить вывод команды с помощью регулярных выражений и получить информацию об устройстве
* записать полученную информацию в файл в CSV формате

Для выполнения задания нужно создать две функции.

Функция parse_sh_version:
* ожидает как аргумент вывод команды sh version одной строкой (не имя файла)
* обрабатывает вывод, с помощью регулярных выражений
* возвращает кортеж из трёх элементов:
 * ios - в формате "12.4(5)T"
 * image - в формате "flash:c2800-advipservicesk9-mz.124-5.T.bin"
 * uptime - в формате "5 days, 3 hours, 3 minutes"

У функции write_inventory_to_csv должно быть два параметра:
 * data_filenames - ожидает как аргумент список имен файлов с выводом sh version
 * csv_filename - ожидает как аргумент имя файла (например, routers_inventory.csv), в который будет записана информация в формате CSV
* функция записывает содержимое в файл, в формате CSV и ничего не возвращает


Функция write_inventory_to_csv должна делать следующее:
* обработать информацию из каждого файла с выводом sh version:
 * sh_version_r1.txt, sh_version_r2.txt, sh_version_r3.txt
* с помощью функции parse_sh_version, из каждого вывода должна быть получена информация ios, image, uptime
* из имени файла нужно получить имя хоста
* после этого вся информация должна быть записана в CSV файл

В файле routers_inventory.csv должны быть такие столбцы:
* hostname, ios, image, uptime

В скрипте, с помощью модуля glob, создан список файлов, имя которых начинается на sh_vers.
Вы можете раскомментировать строку print(sh_version_files), чтобы посмотреть содержимое списка.

Кроме того, создан список заголовков (headers), который должен быть записан в CSV.
'''

import glob
import re
import csv
sh_version_files = glob.glob('sh_vers*')
#print(sh_version_files)

headers = ['hostname', 'ios', 'image', 'uptime']
data_filenames = sh_version_files
csv_filename = 'routers_inventory.csv'

def parse_sh_version(show_version_string):
	ios_r = r'Cisco IOS Software.+?Version (\S+),'
	uptime_r = r'.+?uptime is (.+?)\n'
	image_r = r'.+?System image file is "(\S+)"'
	ios = re.search(ios_r, show_version_string, re.DOTALL).group(1)
	uptime = re.search(uptime_r, show_version_string, re.DOTALL).group(1)
	image = re.search(image_r, show_version_string, re.DOTALL).group(1)
	return(ios, image, uptime)

def write_inventory_to_csv(data_filenames, csv_filename):
	host_list = []
	data_tuple_list = []
	data_list = []
	index = 0
	for elem in data_filenames:
		regex = r'.+_(.+?)\..+'#для определения имени узла
		match = re.findall(regex, elem)
		host_list.append(match[0])
		with open(elem , 'r') as temp:
			show_version_string = temp.read()
			data_tuple_list.append(parse_sh_version(show_version_string))#засовываем в список возврат функции
	for elem in data_tuple_list:#получаем из списка_кортежей список_списков
		data_list.append(list(elem))
	for elem in data_list:#добавляем элементам списка_списков имена узлов из другого списка
		elem.insert(0, host_list[index])
		index += 1
	with open(csv_filename, 'w') as temp:
		writer = csv.writer(temp)
		writer.writerow(headers)
		for elem in data_list:
			writer.writerow(elem)
print(write_inventory_to_csv(data_filenames, csv_filename))
