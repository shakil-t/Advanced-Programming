# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 06:00:02 2017

@author: shakil
"""

s=int(input("Enter the number of elements"))
l=[]
print("Enter the elements")
for a in range(0,s):
    b=int(input())
    if(b%10==5):
        l.append(b)
print(l)