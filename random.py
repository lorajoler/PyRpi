#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 07:47:16 2017

@author: estudis
"""

import random

is_number = False
secret = int(random.uniform(0,10))
print("I'm thinking of a number between zero and ten.", 
      "Can you guess what it is?")

while not is_number:
    is_number = True
    try:
        guess = int (input("Take a guess:"))
    except:
        print ("I said a number")
        is_number = False

while guess != secret:
    guess = int (input ("Take a guess:"))
    
print("Well done!")