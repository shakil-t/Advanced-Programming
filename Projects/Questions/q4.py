# -*- coding: utf-8 -*-
"""
Created on Sun May 21 08:51:14 2017

@author: shakil
"""

s=int(input("Enter the N"))
l=[]
print("Enter the numbers")
for a in range(0,s):
    n=float(input())
    l.append(n)
max=l[0]
for b in range(1,s):
    if(max<l[b]):
        max=l[b]
print("Max value :",max)