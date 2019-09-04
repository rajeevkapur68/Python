# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 11:37:43 2019

@author: rajee
Write a Python program to check whether a specified 
value is contained in a group of values
Test Data :
3 -> [1, 5, 8, 3] : True
-1 -> [1, 5, 8, 3] : False
"""

print((lambda:'False', lambda:'True')  \
        [int((input("input a number: "))) in [1, 5, 8, 3] ] \
      ())
