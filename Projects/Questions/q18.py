# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 21:18:06 2017

@author: shakil
"""

s=int(input("Enter the number of elements"))
l=[]
for a in range(0,s):
    i=int(input())
    l.append(i)
Min1=l[0]
Min2=0
Min3=0
for b in range(1,s):
    if(Min1>l[b]):
        Min3=Min2
        Min2=Min1
        Min1=l[b]
print(Min1,Min2,Min3)
    