# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 06:18:10 2017

@author: shakil
"""

n=int(input("Enter a number"))
l=[]
for a in range(1,n):
    for b in range(2,a):
        if(a%b==0):
           break
        else:
            print(a)