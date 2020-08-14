# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 22:43:48 2018

@author: kumeg
"""

n=int(input("enter a value:"))
l=[]
while(n>0):
    l=l+[n%10]
    n=n//10
l.reverse()
print(l)