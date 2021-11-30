# -*- coding: utf-8 -*-
"""
Created on Sun May 21 09:06:56 2017

@author: shakil
"""

s=int(input("Enter the N"))
sum=0
print("Enter the numbers")
for a in range(0,s):
    n=float(input())
    sum+=n
ave=sum/s
print("Average:",ave)
    
