# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 17:58:28 2019

@author: rajee
 Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
 
"""
myInt = int(input("Input Integer: "))
myInt1 = int("%s%s"%(myInt,myInt))
myInt2 = int("%s%s%s"%(myInt,myInt,myInt))
print(str(type(myInt)) + " , " + str(type(myInt1)) + " , " + str(type(myInt2)))
print("Value of %s+%s+%s is %d" % (myInt,myInt1,myInt2,(myInt+myInt1+myInt2)) )