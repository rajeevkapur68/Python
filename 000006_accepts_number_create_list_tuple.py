# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 15:39:51 2019

@author: rajee
Write a Python program which accepts a sequence of comma-separated numbers from user
and generate a list and a tuple with those numbers.
"""

number_string = input("Input numbers separated by commas : ")

listNumbers = number_string.split(',')
print(listNumbers)
print(type(listNumbers))
tupleNumbers = tuple(listNumbers)
print(tupleNumbers)
print(type(tupleNumbers))
