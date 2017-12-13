#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 08:25:01 2017

@author: estudis
"""

is_number = False
num = 0

while not is_number:
    is_number = True
    try:
        num = int(input("enter a number:" ))
    except ValueError:
        print("I said a number")
        is_number = False

# num = int(input("enter a number: "))

if num % 2 == 0:
    print("your number is divisible by 2")
elif (num % 3 == 0):
    print ("your number is divisible by 3")
elif (num % 5 == 0):
    print("your number is divisible by 5")
else:
    print ("your number isn't divisible by 2, 3 or 5")
