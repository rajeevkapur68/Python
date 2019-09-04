# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 12:48:16 2019

@author: rajee
Write a Python program to create a histogram from a given list of integers.
"""
print("Input integers seperated by space: ")
intList = [int(x)for x in input().split()]
for value in intList:
    myString = ""
    for count in range(value):
        myString += "@"
    print(myString)
    
