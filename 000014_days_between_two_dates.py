# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 19:05:01 2019

@author: rajee
Write a Python program to calculate number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days 
"""
from datetime import date, timedelta
date1 = date(int(input("Input year1: ")),int(input("Input Month1: ")) ,int(input("Input day1: ")) )
print(date1, str(type(date1)))
date2 = date(int(input("Input year2: ")),int(input("Input Month2: ")) ,int(input("Input day2: ")) )

print(date1-date2)
