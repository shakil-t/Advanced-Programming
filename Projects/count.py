# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 19:23:41 2018

@author: shakil
"""

l=["umbrella","flower","rain","pure","как дила?","umbrella","umbrella",
"umbrella","rain","как дила?","как дила?","как дила?","как дила?","как дила?"
,"pure","rain","flower","rain","шакил"]
d={}
for i in l:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)
             
    