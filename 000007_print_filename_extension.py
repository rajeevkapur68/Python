# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 15:49:00 2019

@author: rajee
Write a Python program to accept a filename from the user and 
print the extension of that.

"""
filename = input("Input filename with extension: ")
print("File extension is " + repr(filename.split('.')[-1]))


