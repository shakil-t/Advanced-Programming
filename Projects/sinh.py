# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 09:50:37 2017

@author: shakil
"""

from math import factorial as f
def sinh(x,k):
    k=2*k+1
    a=(x**k)/f(k)
    return a 
x=float(input("Enter a number"))
sum=0
for b in range(0,20):
    sum+=sinh(x,b)
print(sum)
    