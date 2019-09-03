# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 15:20:15 2019

@author: rajee
 Write a Python program which accepts the radius of a circle from the user 
 and compute the area
"""

from math import pi
# by default all inputs are string

r=(input("Input the radius of Circle: "))
print(type(r))

# convert to float at input
r=float(input("Input the radius of Circle: "))
print(type(r))

print("The area of the circle with radius " + str(r) + " = " + str(round((pi*r**2),2)))

