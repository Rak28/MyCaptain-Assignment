# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 22:39:06 2020

@author: Rakshith
"""
        
n = int(input("Enter a number:"))
n1 = 0
n2 = 1

while n1 < n:
    print(n1)
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    
