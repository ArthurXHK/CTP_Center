#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
test ctp
'''
a = 1
def change():
    global a
    a = 2
if __name__ == '__main__':
    change()
    print a