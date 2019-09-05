# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 21:45:24 2019

@author: rajee
Write a Python program to add two objects if both objects are an integer type
"""
x=int(input("Num 1: "))
y=int(input("Num 2:"))

print((lambda:"input number is not an integer", \
       lambda:(x+y))[isinstance(x,int) & isinstance(y,int)]())