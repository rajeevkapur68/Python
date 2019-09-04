# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 06:48:11 2019

@author: rajee
Write a Python program to get the n (non-negative integer) copies of the 
first 2 characters of a given string. Return the n copies of the whole string 
if the length is less than 2
"""
myStr = input("input string: ")
print( (lambda:((myStr[0:2])*int(input("input Copies: "))), \
        lambda:(myStr * int(input("input Copies: ")))) \
        [len(myStr) < 2]()             \
     )