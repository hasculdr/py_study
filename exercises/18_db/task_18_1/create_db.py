# -*- coding: utf-8 -*-
#!/usr/bin/env python3
import os
if os.path.exists('dhcp_snooping.db'):
    print("файл есть")
    print(os.path.exists('dhcp_snooping.db'))
else:
    print("файла нет")
    print(os.path.exists('dhcp_snooping.db'))
