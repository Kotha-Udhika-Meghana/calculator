# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 20:44:17 2018

@author: kumeg
"""

def p(n):
    s=0
    for i in range(1,n):
        if(n%i==0):
            s=s+i
    if(s==n):
        print("given number is perfect number")
    else:
        print("not a perfect number")
n=int(input("enter a value:"))
print(p(n))