# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 17:16:40 2019

@author: rajee
Write a Python program to get the least common multiple (LCM) of 
two positive integers.
https://en.wikipedia.org/wiki/Least_common_multiple
lcm(a,b) = |a-b|/gcd(a,b)
only valid if only one of a or b can be zero.
if both zero then special case lcm(0,0) = 0
"""
def gcd(x,y):
    num =(lambda:int(y/2),lambda:int(x/2))[x > y]()
    for a in range(num,0,-1):
        if(((x % a) == 0) & ((y % a) == 0)):
            return a
            
        
a=int(input("Enter a: "))
b=int(input("Enter b: "))
c=(a*b)/gcd(a,b)
print("LCM is " + str(c))