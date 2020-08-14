# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 21:51:12 2018

@author: kumeg
"""

n=int(input("enter range for fibonacci series::")) 
def fib(n): 
      if(n<2): 
          return 2 
      return (fib(n-1)+fib(n-2)) 
for i in range(n): 
    print("fibonacci of",i,"is",fib(i)) 