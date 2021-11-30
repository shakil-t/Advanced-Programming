# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 06:38:27 2017

@author: shakil
"""

even_sum=0
even_count=0
odd_sum=0
s=int(input("Enter the number of elements"))
for a in range(0,s):
    b=int(input())
    if(b%2==0):
        even_sum+=b
        even_count+=1
    else:
        odd_sum+=b
even_ave=even_sum/even_count
odd_ave=odd_sum/(s-even_count)
if(even_ave>odd_ave):
    print("میانگین اعداد زوج از اعداد فرد بزرگتر است")
else:
    print("میانگین اعداد فرد از اعداد فرد بیشتر است")