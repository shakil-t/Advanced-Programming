# -*- coding: utf-8 -*-
"""
Created on Fri May 26 07:11:00 2017

@author: shakil
"""

sum=0
for a in range(1,1000):
    if(a%3==0 or a%5==0):
        sum+=a
print(sum)