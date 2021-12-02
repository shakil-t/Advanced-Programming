# -*- coding: utf-8 -*-
"""
Created on Fri May 26 07:11:00 2017

@author: shakil
"""

#this code is a solution to the [first problem of projecteuler.net](https://projecteuler.net/problem=1)
#it calculates the sum of all the multiples of 3 or 5 below 1000
sum=0
for a in range(1,1000):
    if(a%3==0 or a%5==0):
        sum+=a
print(sum)
