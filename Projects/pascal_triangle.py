# -*- coding: utf-8 -*-
"""
Created on Tue May 16 13:02:01 2017

@author: shakil
"""

from math import factorial as f
n=int(input("Enter number of the rows"))
for a in range(0,n):
    for c in range(0,a+1):
        p=f(a)/(f(c)*f(a-c))
        print(p,end="\t")
    print("\n")         
