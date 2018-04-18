#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Copyright:    snow
Version:      1.0
email:        snowi@protonmail.com
'''

import os
import sys

path = input('Please enter path:')
os.chdir(path)
print('files and folders in current working dir:'+os.listdir())
a = input('enter y to continue else to exit:')
if a == 'y':
    counter = 1
    for obj in os.listdir():
	    os.rename(obj, '0' + str(counter))#可自定义其他规则
	    counter += 1
else:
    sys.exit()

