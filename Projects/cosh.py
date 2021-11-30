# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 09:46:00 2017

@author: shakil
"""

from math import factorial as f
def cosh(x,k):
    k=2*k
    a=(x**k)/f(k)
    return a 
sum=0
x=float(input("Enter a number"))
for b in range(0,20):
    sum+=cosh(x,b)
print(sum)
