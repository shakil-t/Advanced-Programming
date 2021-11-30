# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 05:55:33 2017

@author: shakil
"""

s=int(input("Enter the number of elements"))
l=[]
print("Enter the elements")
for a in range(0,s):
    b=int(input())
    if(b%3==0):
        l.append(b)
print(l)