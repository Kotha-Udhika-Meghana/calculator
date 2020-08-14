# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 08:09:18 2018

@author: kumeg
"""

s="azcbobobegghakl" 
count=0 
for i in s: 
    if(i=="a" or i=="e" or i=="i" or i=="o" or i=="u"): 
        count=count+1 
print("no of vowels in given string::",count) 