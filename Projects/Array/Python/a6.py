# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 09:01:48 2017

@author: shakil
"""

l1=[5.3,9.78,15,96,93,18]
l1.sort()
l2=[19.5,18,2,-17,25,-87]
l2.sort()
l1.extend(l2)
l1.sort()
print(l1)