# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 19:26:59 2019

@author: rajee
34. Write a Python program to sum of two given integers. 
However, if the sum is between 15 to 20 it will return 20
"""
"""
a=int(input("Number 1:"))
b=int(input("Number 2:"))
print((lambda:(a+b),lambda:20)[((a+b)>=15) & ((a+b)<=20)]())
"""
a=int(input("Number 1:"))
b=int(input("Number 2:"))
print((lambda:(a+b),lambda:20)[(a+b) in range(15,20)]())