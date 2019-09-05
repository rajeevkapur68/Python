# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 20:17:27 2019

@author: rajee
Write a Python program that will return true if the two given integer 
values are equal or their sum or difference is 5
"""

x=int(input("Number 1: "))
y=int(input("Number 2: "))
print((lambda:False,lambda:True)[(x==y) | (abs(x-y)==5) | ((x+y)==5)]())