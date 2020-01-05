# -*- coding: utf-8 -*-
'''
Задание 17.2b

Создать функцию transform_topology, которая преобразует топологию в формат подходящий для функции draw_topology.

Функция ожидает как аргумент имя файла в формате YAML, в котором хранится топология.

Функция должна считать данные из YAML файла, преобразовать их соответственно, чтобы функция возвращала словарь такого вида:
    {('R4', 'Fa 0/1'): ('R5', 'Fa 0/1'),
     ('R4', 'Fa 0/2'): ('R6', 'Fa 0/0')}

Функция transform_topology должна не только менять формат представления топологии, но и удалять дублирующиеся соединения (их лучше всего видно на схеме, которую генерирует draw_topology).

Проверить работу функции на файле topology.yaml. На основании полученного словаря надо сгенерировать изображение топологии с помощью функции draw_topology.
Не копировать код функции draw_topology.

Результат должен выглядеть так же, как схема в файле task_17_2b_topology.svg

При этом:
* Интерфейсы должны быть записаны с пробелом Fa 0/0
* Расположение устройств на схеме может быть другим
* Соединения должны соответствовать схеме
* На схеме не должно быть дублирующихся линков


> Для выполнения этого задания, должен быть установлен graphviz:
> apt-get install graphviz

> И модуль python для работы с graphviz:
> pip install graphviz

'''
from task_17_2a import generate_topology_from_cdp
from pprint import pprint
from draw_network_graph import draw_topology
import yaml

def transform_topology(yaml_file):
	with open(yaml_file, 'r') as data:
		topology = yaml.safe_load(data)
	temp_dict = {}
	topology_items_list = list(topology.items())#ключи и значения словаря собираются в список кортежами
	for elem in topology_items_list:#перебираем все кортежи с вложенными в них двойными словарями
		key = elem[0]#ключ = первая железка
		sub_items = list((elem[1]).items())#собираем вложенные словари в список кортежами
		for elem in sub_items:
			value = elem[0]#значение = порт первой железки
			tuple_key = (key, value)#этот кортеж - ключ словаря для функции draw_topology
			temp_sub_items = list((elem[1]).items())#это список из одного кортежа, будет значением словаря для функции draw_topology
			temp_dict.update({tuple_key: temp_sub_items[0]})#наполняем словарь данными в формате ключ_кортеж: значение_кортеж
	#удаляем дублирующие друг друга элементы
	all_keys = list(temp_dict.keys())#список ключей
	all_values = list(temp_dict.values())#список значений
	for key in all_keys:#проверяем для каждого ключа
		if key in all_values:#если ключ нашелся в списке со значениями
			index = all_values.index(key)#сохраняем индекс значения, равного ключу
			all_values.remove(key)#удаляем такое значение из списка значений
			all_keys.pop(index)#и удаляем по индексу соответствующий ключ из списка ключей
	unique_dict = dict(zip(all_keys, all_values))#получаем новый словарь из обработанных списков
	return(unique_dict)
pprint(transform_topology('topology.yaml'))
print(draw_topology(transform_topology('topology.yaml')))	
