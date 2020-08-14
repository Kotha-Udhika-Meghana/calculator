# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 20:58:22 2018

@author: kumeg
"""

def tables(): 
     for i in range(1,11,1): 
         for j in range(1,11,1): 
       #      print("{:d}*{:d}={:d}".format(i,j,i*j)) 
            print(i,"x",j,"=",i*j) 
tables() 