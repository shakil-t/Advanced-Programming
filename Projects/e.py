# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 09:39:51 2017

@author: shakil
"""

from math import factorial as f
def e(x,k):
    a=(x**k)/f(k)
    return a 
x=float(input("Enter the power"))
sum=0
for b in range(0,20):
    sum+=e(x,b)
print(sum)