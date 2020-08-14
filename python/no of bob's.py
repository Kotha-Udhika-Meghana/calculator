# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 08:11:17 2018

@author: kumeg
"""

s = 'azcbobobegghakl' 
numberofbob=0 
length=int(len(s)) 
x=0 
y=3 
while y<=length:     
    z=s[x:y]     
    if z=='bob':         
        numberofbob+=1    
    else:         
        numberofbob+=0     
        x+=1     
        y+=1 
print("number of times bob occur is: " + str(numberofbob)) 