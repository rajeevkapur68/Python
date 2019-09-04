# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 15:12:06 2019

@author: rajee
Write a Python program to display the current date and time.
"""

import datetime
dt = datetime.datetime.now()
print(dt.strftime("%m-%d-%Y %H:%M:%S"))