# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 08:18:19 2017

@author: shakil
"""

from math import sqrt
l=[]
sum=0
print("Enter the numbers")
for a in range(0,100):
    b=int(input())
    sum+=b
    l.append(b)
m=sum/100
print("Mean:",m)
s=0
for c in range(0,100):
    s+=(l[c]-m)*(l[c]-m)
v=s/100
print("Deviation",sqrt(v))