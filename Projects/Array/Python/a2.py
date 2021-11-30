# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 08:48:56 2017

@author: shakil
"""

p=[]
n=[]
print("Enter the elements")
for a in range(0,100):
    b=int(input())
    if(b>0):
        p.append(b)
    else:
        n.append(b)
print(p)
print(n)