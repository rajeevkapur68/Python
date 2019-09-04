# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 06:20:16 2019

@author: rajee
Write a Python program to count the number 4 in a given list.
"""
from collections import Counter
# Counter makes a dictionary object with keys and value
# keys for elements
# value hold the number of occureneces
print ( "Number 4 appears: " +\
       str((Counter(list(input("input list elements seperated by space: "))))['4']) \
       + " times." \
      )
