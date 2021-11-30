# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 06:17:01 2017

@author: shakil
"""

def Gcd(n,m):
    while(n!=m):
        if(n>m):
            n=n-m
        else:
            m=m-n
    if(n>m):
        return n
    else:
        return m
            
def Lcd(s,t):
    c=s*t
    d=Gcd(s,t)
    return c/d
    
a=int(input("Enter the first number"))
b=int(input("Enter the second number"))
print("Gcd=",Gcd(a,b))
print("Lcd=",Lcd(a,b))


