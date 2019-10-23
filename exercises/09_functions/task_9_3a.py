# -*- coding: utf-8 -*-
'''
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию:
    - добавить поддержку конфигурации, когда настройка access-порта выглядит так:
            interface FastEthernet0/20
                switchport mode access
                duplex auto
      То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
      Пример словаря: {'FastEthernet0/12': 10,
                       'FastEthernet0/14': 11,
                       'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
def get_int_vlan_map(config_filename):
	access_dict = {}
	trunk_dict = {}
	data = (open(config_filename, 'r')).readlines()
	for line in data:
		if line.startswith('interface '):
			temp = (line.strip())[10:]
			#continue
		elif line.startswith(' switchport mode access'):
			access_dict[temp] = 1
		elif line.startswith(' switchport access vlan'):
			access_dict[temp] = int(line[23:-1])
		elif line.startswith(' switchport trunk allowed vlan'):
			allowed_list_str = (line[31:-1]).split(',')
			allowed_list_int = []
			for elem in allowed_list_str:
				allowed_list_int.append(int(elem))
			trunk_dict[temp] = allowed_list_int
	return(access_dict, trunk_dict)
print(get_int_vlan_map('config_sw2.txt'))
