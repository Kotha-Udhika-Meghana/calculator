# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 19:04:45 2018

@author: kumeg
"""

n=int(input("enter any number::")) 
if (n==1): 
    print(n,"IS NOT A PRIME") 
elif (n==2 or n==3 or n==5 or n==7 or n==11): 
          print(n,"IS PRIME")     
elif (n%2==0 or n%3==0 or n%5==0 or n%7==0 or n%11==0): 
          print(n,"IS NOT A PRIME") 
else: 
      print(n,"IS A PRIME") 
  