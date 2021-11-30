# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 08:52:30 2017

@author: shakil
"""

l=[]
print("Enter the elements")
for a in range(0,20):
    b=int(input())
    l.append(b)
max=l[0]
for c in range(1,20):
    if(l[c]>max):
        max=l[c]
for d in range(0,20):
    if(max==l[d]):
        print(d)