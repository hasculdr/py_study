#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from pprint import pprint
from create_db import filecheck
import sqlite3
import yaml
import re
import glob

def yaml_read_and_convert(yamlfile):
	with open(yamlfile, 'r') as data:
		py_object = yaml.safe_load(data)
	return(py_object)
		

def switches_table_update(subdict):
	keys_list_from_subdict = list(subdict.keys())#собираем в список ключи вложенного словаря
	connection = sqlite3.connect('dhcp_snooping.db')
	for key in keys_list_from_subdict:
		value = subdict[key]#сохраняем значение для текущего ключа
		try:
			connection.execute(f'INSERT into switches values ("{key}", "{value}");')
		except sqlite3.IntegrityError as error:
			print(f'При добавлении данных: {(key, value)} возникла ошибка: ', error)
	connection.commit()#подтверждаем операцию в БД
	connection.close()

def text_read_and_convert(textfile):
	hostname = (re.match('(.*?)_.*', textfile)).groups()#получаем имя устройства из имени файла
	with open(textfile, 'r') as text:
		data = text.read()
		regexp = (r'(\S+?)\s+'#mac-адрес
				   '(\S+?)\s+'#ip-адрес
				   '\d+?\s+'#lease(sec)
				   '\S+?\s+'#type
				   '(\d+?)\s+'#vlan
				   '(\S+)')#interface
		dhcp_data = re.findall(regexp, data)
		temp_list = []#пустой список для данных из кортежа
		result_list = []#пустой список для данных, добавляемых в БД
		for list_elem in dhcp_data:#для каждого кортежа в списке
			temp_list = list(list_elem)#присваиваем временному списку данные кортежа
			temp_list.append(hostname[0])#когда кортеж преобразован в список - добавляем в конец имя узла
			result_list.append(temp_list)#собираем итоговый список списков для добавления в БД
	return(result_list)#возвращается вложенный список

def dhcp_table_update(elem):
	connection = sqlite3.connect('dhcp_snooping.db')
	try:
		connection.execute(f'INSERT into dhcp values ("{elem[0]}", "{elem[1]}", "{elem[2]}", "{elem[3]}", "{elem[4]}");')
	except sqlite3.IntegrityError as error:
		print(f'При добавлении данных: {tuple(elem)} возникла ошибка: ', error)
	connection.commit()#подтверждаем операцию в БД
	connection.close()

if __name__ == '__main__':
	if not filecheck('dhcp_snooping.db'):#если БД не существует (значение проверки - ложь)
		print('База данных не существует. Создайте ее с помощью скрипта "create_db".')
	else:
		print('Добавляю данные в таблицу "switches"...')
		two_level_dict = yaml_read_and_convert('switches.yml')
		subdict = two_level_dict['switches']
		switches_table_update(subdict)
		dhcp_snooping_files = glob.glob('*_dhcp_snooping.txt')#получаем список имен файлов, которые нужно обработать
		print('Добавляю данные в таблицу "dhcp"...')
		for elem in dhcp_snooping_files:#несколько вложенных списков
			sublist = text_read_and_convert(elem)
			for elem in sublist:
				dhcp_table_update(elem)
