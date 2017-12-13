#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 08:45:42 2017

@author: estudis
"""

def biggest(a,b):
    if (a > b):
        return a
    elif (a < b):
        return b

print ("The biggest of 2 and 3 is ", biggest(2,3))
print ("The biggest of 10 and 5 is ", biggest(10,5))