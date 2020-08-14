# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 18:38:01 2018

@author: kumeg
"""

l=[] 
sum=0 
while(True): 
    n=int(input("enter no::")) 
    l.append(n)        
    if (n==0): 
        print("sum of all nos entered::") 
        for j in (l): 
            sum=sum+j 
        print(sum) 
        break 
    else: 
        continue 
  