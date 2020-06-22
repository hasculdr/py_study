# -*- coding: utf-8 -*-
"""
Задание 21.1

Создать функцию generate_config.

Параметры функции:
* template - путь к файлу с шаблоном (например, "templates/for.txt")
* data_dict - словарь со значениями, которые надо подставить в шаблон

Функция должна возвращать строку с конфигурацией, которая была сгенерирована.

Проверить работу функции на шаблоне templates/for.txt и данных из файла data_files/for.yml.

"""
import yaml
from jinja2 import Environment, FileSystemLoader


def generate_config(template, data_dict):
	template_loader_args=path.split('/')
	env=Environment(loader=FileSystemLoader(template_loader_args[0]))
	template=env.get_template(template_loader_args[1])
	return(template.render(data_dict))


path='templates/for.txt'


if __name__=="__main__":
	with open('data_files/for.yml', 'r') as f:
		data_dict=yaml.safe_load(f)
	print(generate_config(path, data_dict))
