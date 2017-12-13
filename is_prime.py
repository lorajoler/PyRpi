#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 08:12:13 2017

@author: estudis
"""

for i in range (1, 300000, 2):
    is_prime = True
    for k in range (2, i):
        if (i % k) == 0:
            print (i , " is divisible by ", k)
            is_prime = False
            break
    if is_prime:
        print(i, "is_prime")
    
            