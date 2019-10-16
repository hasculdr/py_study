# -*- coding: utf-8 -*-
'''
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости от выбранного режима,
задавались разные вопросы в запросе о номере VLANа или списка VLANов:
* для access: 'Введите номер VLAN:'
* для trunk: 'Введите разрешенные VLANы:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
'''

access_template = [
    'switchport mode access', 'switchport access vlan {}',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]

trunk_template = [
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk allowed vlan {}'
]
mode = input('Введите режим работы интерфейса (access/trunk): ')
interface = input('Введите тип и номер интерфейса: ')
access_input = 'Введите номер VLAN: '
trunk_input = 'Введите разрешенные VLANы: '
vlans_input = dict(access = access_input, trunk = trunk_input)
vlan = input(f'{vlans_input[mode]}')
access_value = ('\n'.join(access_template))
trunk_value = ('\n'.join(trunk_template))
settings = dict(access = access_value, trunk = trunk_value)
print(f'''Interface {interface}
{settings[mode].format(vlan)}''')
