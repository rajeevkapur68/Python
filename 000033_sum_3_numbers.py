# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 19:07:21 2019

@author: rajee
Write a Python program to sum of three given integers. 
However, if two values are equal sum will be zero.
"""
x=int(input("Enter Num1: "))
y=int(input("Enter Num2: "))
z=int(input("Enter Num3: "))
if((x==y) | (x==z) | (y==z)):
    print("sum = ", 0)
else:
    print("sum = ", x + y + z)
