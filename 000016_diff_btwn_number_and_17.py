# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 21:08:53 2019

@author: rajee
Write a Python program to get the difference between a given number and 17,
 if the number is greater than 17 return double the absolute difference. 
 if answer number negative, make it absolute, else double it.
"""
x= int(input("Input Number: "))    #((17-x)*2 )    abs(x - 17)
#(f,t)[a<b]
print("Difference between %i and 17 is %d " % (x, (((x - 17)*2 ) ,abs(x - 17) ) [x < 17] ))