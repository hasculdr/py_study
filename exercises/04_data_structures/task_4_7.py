# -*- coding: utf-8 -*-
'''
Задание 4.7

Преобразовать MAC-адрес mac в двоичную строку такого вида:
'101010101010101010111011101110111100110011001100'

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

mac = 'AAAA:BBBB:CCCC'
temp_str = mac.replace(':', '')
temp = (f'{bin(int(temp_str[0], 16))}{bin(int(temp_str[1], 16))}{bin(int(temp_str[2], 16))}{bin(int(temp_str[3], 16))}{bin(int(temp_str[4], 16))}{bin(int(temp_str[5], 16))}{bin(int(temp_str[6], 16))}{bin(int(temp_str[7], 16))}{bin(int(temp_str[8], 16))}{bin(int(temp_str[9], 16))}{bin(int(temp_str[10], 16))}{bin(int(temp_str[11], 16))}')
print(temp.replace('0b', ''))
