# -*- coding: utf-8 -*-
"""
Created on Sat May 20 21:28:07 2017

@author: shakil
"""

a=int(input("Enter the division"))
b=int(input("Enter the divisor(except zero)"))
count=0
while(a>b or a==b):
    a=a-b
    count+=1
print("Quotient:",count)
print("Remainder:",a)
