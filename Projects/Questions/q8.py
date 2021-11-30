# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 04:06:26 2017

@author: shakil
"""

Nonzero=False
l=[]
print("Enter the numbers")
while(Nonzero==False):
    a=int(input())
    if(a==0):
        Nonzero=True
    elif(a%10==3):
        l.append(a)
print(l)