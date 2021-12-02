# -*- coding: utf-8 -*-
"""
Created on Sun May  7 08:09:18 2017

@author: shakil
"""

a=int(input("Enter the first number"))
b=int(input("enter the second number"))
c=a+b
print("The Summation equals to :",c)
#Summation of two variables
c=a-b
print("The Subtraction equals to :",c)
#Subtraction of two variables
c=a*b
print("The Multiplication equals to :",c)
#Multiplication of two variables
c=a/b
print("The Division equals to :",c)
#Division of two variables
c=a**b
print("%s powered by %s equals to :"%(a,b),c)
c=a%b
if (c==0):
    print("0")
elif (c==1):
    print("1")
else:
    print("2")
