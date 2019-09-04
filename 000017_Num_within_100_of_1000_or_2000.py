# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 22:40:32 2019

@author: rajee
Write a Python program to test whether a number is within 100 of 1000 or 2000
"""

x = int(input("Input Number: "))
#(False, True)[a<b]
print( (False,True)[(abs(1000-x)<=100) or (abs(2000-x)<=100)] )

