# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 10:12:35 2017

@author: shakil
"""

#I am not sure why I developed this code
import math
l=[23, 41, 69, 123, 137, 247, 411, 943, 2829, 3151, 5617, 9453, 16851, 129191, 387573]
for a in l:
    b=int(math.sqrt(a))
    for c in range(3,b):
        if b%c==0:
            l.remove(a)
            break

print(l)
