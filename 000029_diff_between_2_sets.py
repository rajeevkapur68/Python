# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 16:37:48 2019

@author: rajee
https://www.w3resource.com/python-exercises/python-basic-exercises.php

29. Write a Python program to print out a set containing all the colors from 
color_list_1 which are not present in color_list_2. Go to the editor
Test Data :
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
Expected Output :
{'Black', 'White'}
"""

color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])

print(color_list_1.difference(color_list_2))




