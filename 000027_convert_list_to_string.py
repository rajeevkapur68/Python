# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 13:05:02 2019

@author: rajee
Write a Python program to concatenate all elements in a list into 
a string and return it
"""
# input into a list of integers
#print([int(x) for x in input()])

# input into a list of strings
print("enter data for list: example abcd or 34567 ")
y=[x for x in input()]
print(y)
print(''.join(y))