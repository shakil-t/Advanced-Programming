# -*- coding: utf-8 -*-
"""
Created on Fri May 26 07:21:55 2017

@author: shakil
"""

#this code is a solution to the [second problem of projecteuler.net](https://projecteuler.net/problem=2)
#it calculates the sum of even-valued terms in the Fibonacci sequence
n1=1
n2=2
n3=0
sum=2
for a in range(0,30):
    n3=n1+n2
    if(n3%2==0):
        sum+=n3
    n1=n2
    n2=n3
print(sum)
