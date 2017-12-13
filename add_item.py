#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 13:41:29 2017

@author: estudis
"""
import copy
def add_item(list_1):
    list_1.append(1)
    return list_1

list2 = [2, 3,4]
list3 = add_item(copy.deepcopy(list2))
print("list2:", list2)
print("list3:", list3)