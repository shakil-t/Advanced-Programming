# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 08:26:03 2017

@author: shakil
"""

l=[]
counter=0
print("Enter the numbers")
for b in range(0,20):
    b=input()
    l.append(b)
d=input(("Enter the number you want to search for"))
for c in l:
    if(d==c):
        counter+=1
print(d,":",counter)
