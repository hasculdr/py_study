#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sqlite3

def filecheck(dbname):
    if os.path.exists(dbname):#если БД существует - истина
        return(True)
    else:#не существует - ложь
        return(False)


def dbcreate(dbname, schema):
    with open(schema, 'r') as file:
        commands = file.read()
    connection = sqlite3.connect(dbname)#создаем соединение с новой БД
    connection.executescript(commands)#выполняем команды схемы
    connection.close()#закрываем соединение с БД



if __name__ == '__main__':
    if not filecheck('dhcp_snooping.db'):#если БД не существует (значение проверки - ложь)
        print('Создаю базу данных...')
        dbcreate('dhcp_snooping.db', 'dhcp_snooping_schema.sql')
    else:
        print('База данных существует')
