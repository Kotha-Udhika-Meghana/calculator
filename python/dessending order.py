# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 08:02:53 2018

@author: kumeg
"""

def selectionSort(alist): #defining alist 
   for l in range(len(alist)-1,0,-1): 
       i=0 
       #print(alist) #checking 
       for j in range(1,l+1): 
           if alist[j]>alist[i]: 
               i = j 
 
       temp = alist[l] 
       alist[l] = alist[i] 
       alist[i] = temp 
 
alist = [54,26,93,17,77,31,44,55,20] 
selectionSort(alist) 
print(alist) 
print("descending order::",alist[::-1]) 