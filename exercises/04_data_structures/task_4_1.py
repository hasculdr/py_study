# -*- coding: utf-8 -*-
'''
Задание 4.1

Обработать строку nat таким образом,
чтобы в имени интерфейса вместо FastEthernet было GigabitEthernet.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

#nat = 'ip nat inside source list ACL interface FastEthernet0/1 overload'
#nat_m = nat.replace('Fast', 'Gigabit')
#print(nat_m)

a = '1234567890'
b = '24'
if b in a:
	print(b)
else:
	print('не найдено')
