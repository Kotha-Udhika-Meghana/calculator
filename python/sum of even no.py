# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 20:38:10 2018

@author: kumeg
"""

n=int(input("enter the limit::")) 
def even(n):     
      for i in range(2,n+1,2): 
          print(i,end=",") 
even(n) 