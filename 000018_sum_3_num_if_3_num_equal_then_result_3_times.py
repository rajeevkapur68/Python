# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 22:53:46 2019

@author: rajee
Write a Python program to calculate the sum of three given numbers, 
if the values are equal then return three times of their sum.
"""
x1,x2,x3=int(input("Number 1: ")),int(input("Number 2: ")),int(input("Number 3: "))

print( ((x1+x2+x3),3*(x1+x2+x3))[x1==x2==x3]   )
