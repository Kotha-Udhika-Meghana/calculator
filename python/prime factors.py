# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 21:49:58 2018

@author: kumeg
"""

n=int(input("enter any number::")) 
l=[] 
def factors(n): 
    for i in range(1,n+1): 
        if(n%i==0): 
            l.append(i) 
factors(n) 
print("factors of",n,"are::",l)          
if(len(l)==2): 
    print(n,"is prime") 
else: 
    print(n,"is not prime") 