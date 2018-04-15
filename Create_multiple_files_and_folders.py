#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Copyright:    snow
Version:      1.0
email:        snowi@protonmail.com
'''

import os
import sys

class generator:
    def __init__(self, path, number):
        self.p = path
        self.n = number
    def gendir(self):
        os.chdir(self.p)
        for i in range(int(self.n)):
            folder_name = '0' + str(i)
            if os.path.exists(folder_name):
                pass
            else:
                os.mkdir(folder_name)

    def genfile(self):
        os.chdir(self.p)
        for i in range(int(self.n)):
            file_name = '0' + str(i) + '.txt'
            if os.path.exists(file_name):
                pass
            else:
                f = open(file_name, 'a')
                f.close()
	
if __name__ == '__main__':
    path = input('Please enter path:')
    number = input('Please enter number:')
    gen = generator(path, number)
    times = 0
    while times < 3:
        choice = input('Please enter 1 to create folders or 2 to create files:')
        if choice == '1':
            gen.gendir()
            break
        elif choice == '2':
            gen.genfile()
            break
        else:
            print('Please enter right number!')
            times += 1
    else:
        print('You tried too many times!')
	
	
