# -*- coding: utf-8 -*-
"""
Created on Fri May  5 07:10:56 2017

@author: shakil
"""

list=["happy",[2,0,12.537,0.000896,5]]
print(list[0][2])
print(list[1][3])
#Accessing elements from a list 
print(list[0][-1])
#Negative indexing
print(list[0][2:4])
#Slicing a list 
list.append("excited")
list.extend([2,"t"])
list.insert(1,5)
list.pop(2)
list.clear()

tuple=("mouse", [8, 4, 6], (1, 2, 3))
print(type(tuple))
print(tuple)
print(("repeat",)*5)
#Repeating the elements in a tuple for a given number of times using the * operator
print(tuple.count("m"))
for name in ("Katy","Tracy"):
    print ("Hello",name,"!")

dict={'name': 'John', 1: [2, 4, 3]}
print(dict['name'])
dict[1]=[0.0256,2,3,4,77]
del dict[1]
dict.copy()

set={7.0,"love",(3,2,1)}
frozenset={"orange","pomegranate","grapefruit"}
"""Set is mutable unlike frozenset"""
