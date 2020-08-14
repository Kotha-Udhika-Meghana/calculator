# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 19:08:20 2018

@author: kumeg
"""

n=6 
for i in range(1,n): 
    for j in range(0,i): 
        print("*",end="    ") 
    print("\n") 
for i in range(1,n): 
    for j in range(n,i+1,-1): 
         print("*",end="    ") 
    print("\n")     