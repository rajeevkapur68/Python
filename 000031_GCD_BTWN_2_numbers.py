# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 16:54:31 2019

@author: rajee
31. Write a Python program to compute the greatest common divisor (GCD) of 
two positive integers. 
"""
num1=int(input("Enter Number1:"))
num2=int(input("Enter Number2:"))
num3=(lambda:int(num2/2),lambda:int(num1/2))[num1 > num2]()
print(num3)

for x in range(num3,0,-1):
    if(((num1 % x) == 0) & ((num2 % x) == 0)):
        gcd = x
        break
    
print("GCD is " + str(gcd))
