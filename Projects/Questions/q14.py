# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 04:14:54 2017

@author: shakil
"""

s=int(input("Enter the number of elements"))
l=[]
for a in range(0,s):
    b=int(input())
    l.append(b)
increase=True
decrease=True
for c in range(0,s-1):
    if(increase==True and l[c]>l[c+1]):
        increase=False
    if(decrease==True and l[c]<l[c+1]):
        decrease=False
if(increase==decrease):
    print("Untidy")
    else:
        if(increase==True and decrease==False):
            print("Tidy,Increasing")
            else:
                print("Tidy,Decreasing")