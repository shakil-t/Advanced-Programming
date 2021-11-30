# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 09:58:08 2017

@author: shakil
"""

from math import factorial as f
def sin(x,k):
    t=2*k+1
    a=(((-1)**k)*(x**t))/f(t)
    return a
x=float(input("Enter an angle"))
sum=0
for b in range(0,20):
    sum+=sin(x,b)
print(sum)