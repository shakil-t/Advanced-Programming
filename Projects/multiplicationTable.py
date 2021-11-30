# -*- coding: utf-8 -*-
"""
Created on Fri May 12 07:38:02 2017

@author: shakil
"""

r=int(input("Enter the number of rows"))
c=int(input("Enter the number of columns"))
for i in range(1,r+1):
    for j in range(1,c+1):
        print(i*j,end="\t")
    print("\n")
