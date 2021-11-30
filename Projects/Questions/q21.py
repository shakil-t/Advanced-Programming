# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 08:12:00 2017

@author: shakil
"""

Upper=int(input("Enter the upper range"))
print("2")
for num in range(3,Upper):
    for a in range(2,num):
        if(num%a==0):
            break
        else:
            print(num)