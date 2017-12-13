#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 22:23:44 2017

@author: estudis
"""

class Person():
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def birthday(self):
        self.age = age + 1
        
class Parent(Person):
    def __init__(self, age, name):
        Person.__init__(self, age, name)
        self.children = []
        
    def add_child(self, child):
        self.children.append(child)
        
    def print_children(self):
        print("The children of ", self.name, " are:")
        for child in self.children:
            print(child.name)
    
john = Parent(60, "John")
ben = Person(31, "Ben")
print (john.name, john.age)
print(ben.name, ben.age)
john.add_child(ben)
john.print_children()