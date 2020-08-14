# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 18:26:43 2018

@author: kumeg
"""

a=float(input("enter no::")) 
b=float(input("enter no::")) 
c=float(input("enter no::")) 
d=(b**2)-(4*a*c) 
e=d**(1/2) 
f=(-b+(e))/(2*a) 
r=(-b-(e))/(2*a) 
if(d>0): 
    print("roots are real and not equal") 
elif(d==0): 
    print("roots are real and equal ") 
else: 
    print("roots are imaginary")     
 
print('The solution are {0} and {1}'.format(f,r))