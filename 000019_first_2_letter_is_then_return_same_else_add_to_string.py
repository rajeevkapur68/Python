# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 23:05:32 2019

@author: rajee
Write a Python program to get a new string from a given string where "Is" has 
been added to the front. If the given string already begins with "Is" then 
return the string unchanged.
"""
inpStr = input("Input String: ")
#print(inpStr[0:2]=='Is')
print( (str("Is%s"%inpStr ),inpStr)[inpStr[0:2]=='Is']   )
