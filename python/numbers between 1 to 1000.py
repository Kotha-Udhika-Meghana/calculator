# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 18:51:00 2018

@author: kumeg
"""

s=[] 
for i in range(1,1000+1): 
      if(i//2!=0 and i//3!=0 and i//5!=0 and i//7!=0 and i//11!=0 and i//13!=0 and i//17!=0 and i//19!=0): 
            s.append(i) 
print(s) 
