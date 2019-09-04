# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 06:08:32 2019

@author: rajee
Write a Python program to find whether a given number (accept from the user) is
even or odd, print out an appropriate message to the user.
"""
#(lambda:"false",lambda:"true")[a<b] ()
print( (lambda:"Odd Number", lambda:"Even Number") \
        [(abs(int(input("Input number: ")))%2 == 0)] ()  \
     )
