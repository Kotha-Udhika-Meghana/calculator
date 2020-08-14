# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 07:55:36 2018

@author: kumeg
"""

def bubbleSort(alist): 
    for i in range(len(alist)): 
        for j in range(0,len(alist)-i-1): 
            #print(alist) #for checking progress 
            if alist[j]>alist[j+1]: 
                temp = alist[j] 
                alist[j] = alist[j+1] 
                alist[j+1] = temp 
 
alist = [54,26,93,17,77,31,44,55,20] 
bubbleSort(alist) 
print(alist) 
 