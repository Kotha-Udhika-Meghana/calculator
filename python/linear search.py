# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 07:51:41 2018

@author: kumeg
"""

n=[1,45,563,2,356,66] 
position=-1 
key=int(input('Enter the number you want to search: ')) 
for i in range(len(n)):     
    if n[i]==key:         
        position=i 
 
if(position==-1):     
    print('Number not found in the list.') 
else:     
    print('Number found at position ',position+1) 