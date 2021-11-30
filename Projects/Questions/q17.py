# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 06:38:28 2017

@author: shakil
"""

n=int(input("Enter a number"))
sum=0
while(n>0):
    sum+=n%10
    n=int(n/10)
if(sum%9==0):
    print("This number is divisible by 9")
else:
    print("This number is not divisble by 9")