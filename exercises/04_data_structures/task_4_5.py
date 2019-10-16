# -*- coding: utf-8 -*-
'''
Задание 4.5

Из строк command1 и command2 получить список VLANов,
которые есть и в команде command1 и в команде command2.

Результатом должен быть список: ['1', '3', '8']

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

command1 = 'switchport trunk allowed vlan 1,2,3,5,8'
command2 = 'switchport trunk allowed vlan 1,3,8,9'
com1_list = command1.split()
com1_vlans = com1_list[-1]
vlan_list1 = com1_vlans.split(',')
com2_list = command2.split()
com2_vlans = com2_list[-1]
vlan_list2 = com2_vlans.split(',')
set1 = set(vlan_list1)
set2 = set(vlan_list2)
result_set = set1 & set2
result_list = list(result_set)
sorted_list = sorted(result_list)
print(sorted_list)
