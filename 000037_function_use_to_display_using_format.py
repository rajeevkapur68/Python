# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 04:54:34 2019

@author: rajee
Write a Python program to display your details like 
name, age, address in three different lines using function.

Sample Output: 
Name: Simon                                                                                                   
Age: 19                                                                                                       
Address: Bangalore, Karnataka, India
"""

def personaldetails():
    name, age = 'Simon', 19
    address = 'Bangalore, Karnataka, India'
    print("Name: {}\nAge: {}\nAddress: {}".format(name,age,address))
    
personaldetails()