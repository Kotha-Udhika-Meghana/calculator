# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 21:37:54 2018

@author: kumeg
"""

n=int(input("enter the limit::")) 
def power(n): 
    sum=0 
    for i in range(1,n+1): 
            a=i**5 
            sum=sum+a 
    return sum 
print("sum of n**5=",power(n)) 