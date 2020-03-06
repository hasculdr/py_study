# -*- coding: utf-8 -*-
#!/usr/bin/env python3

from create_db import filecheck
import sqlite3
import yaml
import re

def yaml_read_and_convert(yamlfile):
	with open(yamlfile, 'r') as data:
		py_object = yaml.safe_load(data)
	return(py_object)
		

def switches_table_update(subdict):
	keys_list_from_subdict = list(subdict.keys())#собираем в список ключи вложенного словаря
	connection = sqlite3.connect('dhcp_snooping.db')
	for key in keys_list_from_subdict:
		value = subdict[key]#сохраняем значение для текущего ключа
		connection.execute(f'INSERT into switches values ("{key}", "{value}");')
	connection.commit()#подтверждаем операцию в БД
	connection.close()

#def dhcp_table_update():
	

if __name__ == '__main__':
	if not filecheck('dhcp_snooping.db'):#если БД не существует (значение проверки - ложь)
		print('База данных не существует. Создайте ее с помощью скрипта "create_db".')
	else:
		print('Добавляю данные в таблицу "switches"...')
		two_level_dict = yaml_read_and_convert('switches.yml')
		subdict = two_level_dict['switches']
		switches_table_update(subdict)
		print('Добавляю данные в таблицу "dhcp"...')
	#print(keys_list_from_subdict)
	#print('--------------')
	#print(subdict)
	#print('--------------')
	#for elem in keys_list_from_subdict:
	#	print(subdict[elem])






#получить ключи
#по ключам добавлять данные в таблицу
