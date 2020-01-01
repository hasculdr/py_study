# -*- coding: utf-8 -*-
'''
Задание 15.1b

Проверить работу функции get_ip_from_cfg из задания 15.1a на конфигурации config_r2.txt.

Обратите внимание, что на интерфейсе e0/1 назначены два IP-адреса:
interface Ethernet0/1
 ip address 10.255.2.2 255.255.255.0
 ip address 10.254.2.2 255.255.255.0 secondary

А в словаре, который возвращает функция get_ip_from_cfg, интерфейсу Ethernet0/1
соответствует только один из них (второй).

Скопировать функцию get_ip_from_cfg из задания 15.1a и переделать ее таким образом, чтобы она возвращала список кортежей для каждого интерфейса.
Если на интерфейсе назначен только один адрес, в списке будет один кортеж.
Если же на интерфейсе настроены несколько IP-адресов, то в списке будет несколько кортежей.

Проверьте функцию на конфигурации config_r2.txt и убедитесь, что интерфейсу
Ethernet0/1 соответствует список из двух кортежей.

Обратите внимание, что в данном случае, можно не проверять корректность IP-адреса,
диапазоны адресов и так далее, так как обрабатывается вывод команды, а не ввод пользователя.

'''
import re
from pprint import pprint
def get_ip_from_cfg(config):
	with open(config, 'r') as config_file:
		data = config_file.read()
		regex_intf_conf = r'\ninterface \S+?.+?!'#сохраняем конфиги интерфейсов
		regex_intf_name = r'interface (\S+)'#сохраняем имена интерфейсов
		regex_intf_addr = r'ip address (\d+\.\d+\.\d+\.\d+) (\d+\.\d+\.\d+\.\d+).*\n?'#сохраняем ip-адреса
		intf_conf = re.findall(regex_intf_conf, data, re.DOTALL)
		intf_name = []#для добавления совпадений имен интерфейсов в цикле
		intf_addr = []#аналогично для ip-адресов
		for elem in intf_conf:
			intf_name.append(re.findall(regex_intf_name, elem))
			intf_addr.append(re.findall(regex_intf_addr, elem))
		temp_var = list(zip(intf_name, intf_addr))
		output_dict = {}
		for elem in temp_var:
			if [] in elem:	
				continue
			else:
				output_dict[str(elem[0][0])] = list(elem[1])#выковыриваем неадекватно вложенный ключ (ключ в списке, список в кортеже) 
		return(output_dict)
if __name__ == "__main__":
	pprint(get_ip_from_cfg('config_r2.txt'))
