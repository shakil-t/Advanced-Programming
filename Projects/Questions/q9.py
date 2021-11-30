# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 06:11:44 2017

@author: shakil
"""

n=int(input("Enter a number"))
for a in range(1,n+1):
    if(n%a==0):
        print(a,end="\t")