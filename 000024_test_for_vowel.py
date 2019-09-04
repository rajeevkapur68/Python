# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 07:07:44 2019

@author: rajee
Write a Python program to test whether a passed letter is a vowel or not.
"""



x =  input("Enter a char: ")
print((lambda:"Enter only one character" , \
       lambda: \
                   (lambda:'Not a Vowel', lambda:'its a Vowel') \
                   [x in ['a','e','i','o','u','A','E','I','O','U']]() \
                   \
      )[len(x) < 2]() \
     )