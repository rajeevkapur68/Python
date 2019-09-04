# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 18:11:34 2019

@author: rajee
Write a Python program to print the documents (syntax, description etc.) 
of Python built-in function(s).
"""

x = input("Input built in function name for syntax and description: ") + str('.__doc__') 
print(eval(x))