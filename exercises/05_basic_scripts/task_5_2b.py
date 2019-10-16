#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Задание 5.2b

Преобразовать скрипт из задания 5.2a таким образом,
чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
from sys import argv

prefixes = {'0': '0.0.0.0',
			'1': '128.0.0.0',
			'2': '192.0.0.0',
			'3': '224.0.0.0',
			'4': '240.0.0.0',
			'5': '248.0.0.0',
			'6': '252.0.0.0',
			'7': '254.0.0.0',
			'8': '255.0.0.0',
			'9': '255.128.0.0',
			'10': '255.192.0.0',
			'11': '255.224.0.0',
			'12': '255.240.0.0',
			'13': '255.248.0.0',
			'14': '255.252.0.0',
			'15': '255.254.0.0',
			'16': '255.255.0.0',
			'17': '255.255.128.0',
			'18': '255.255.192.0',
			'19': '255.255.224.0',
			'20': '255.255.240.0',
			'21': '255.255.248.0',
			'22': '255.255.252.0',
			'23': '255.255.254.0',
			'24': '255.255.255.0',
			'25': '255.255.255.128',
			'26': '255.255.255.192',
			'27': '255.255.255.224',
			'28': '255.255.255.240',
			'29': '255.255.255.248',
			'30': '255.255.255.252',
			'31': '255.255.255.254',
			'32': '255.255.255.255'}

arr = argv[1].split('/')
ip_octets = arr[0].split('.')
mask_octets = prefixes[arr[1]].split('.')
input_ip_binary = f'{int(ip_octets[0]):08b}{int(ip_octets[1]):08b}{int(ip_octets[2]):08b}{int(ip_octets[3]):08b}'
mask_binary = f'{int(mask_octets[0]):08b}{int(mask_octets[1]):08b}{int(mask_octets[2]):08b}{int(mask_octets[3]):08b}'
zeroes = (int(mask_binary.count('0')))
output_net_part = input_ip_binary[0:(32-zeroes)]
output_host_part = '0'*zeroes
output_net_ip_binary = output_net_part+output_host_part
output_net_ip_decimial = f'{int(output_net_ip_binary[0:8], 2)}.{int(output_net_ip_binary[8:16], 2)}.{int(output_net_ip_binary[16:24], 2)}.{int(output_net_ip_binary[24:], 2)}'
output_net_ip_octets = output_net_ip_decimial.split('.')
print(f'''Network:
{output_net_ip_octets[0]:8} {output_net_ip_octets[1]:8} {output_net_ip_octets[2]:8} {output_net_ip_octets[3]:8}
{output_net_ip_binary[0:8]} {output_net_ip_binary[8:16]} {output_net_ip_binary[16:24]} {output_net_ip_binary[24:]}

Mask:
/{arr[1]}
{mask_octets[0]:8} {mask_octets[1]:8} {mask_octets[2]:8} {mask_octets[3]:8}
{int(mask_octets[0]):08b} {int(mask_octets[1]):08b} {int(mask_octets[2]):08b} {int(mask_octets[3]):08b}''')
