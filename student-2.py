#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 08:33:48 2017

@author: estudis
"""

student_data= [["Ben", {"Maths": 67, "English": 78, "Science": 72}],
               ["Mark", {"Maths": 56, "Art": 64, "History": 39, "Geography": 55}],
               ["Paul", {"English": 66, "History": 88}]]

grades = ((0, "FAIL"),(50, "D"),(60,"C"),(70, "B"), (80,"A"), (101, "CHEAT!"))

class Student():
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        
    def print_report_card(self):
        print("Report card for student ", self.name)
        for subject, mark in self.marks.items():
            for i in grades:
                if mark < i[0]:
                    print(subject, " : ", prev_grade)
                    break
                prev_grade = i[1]
                
    def add_mark(self, subject, mark):
        if subject in self.marks.keys():
            print(student_name, " already has a mark for ", subject)
            user_input = input("Overwrite Y/N? ")
            if user_input == "Y" or "y":
                self.marks[subject] = mark
                return "Student's mark updated"
            else:
                return "Student's mark not updated"
        else:
            self.marks[subject] = mark
            return "Student's mark added"
    
class Students():
    def __init__(self, all_students):
        self.students = []
        for student, mark in all_students:
            self.add_student(student, mark)
            
    def add_student(self,student_name, marks = {}):
        if self.exists(student_name):
            return "Student already in database"
        else:
            self.students.append(Student(student_name, marks))
            return "Student added"
        
    def print_report_cards(self, student_name = None):
        for student in self.students:
            if student_name == None or student.name:
                student.print_report_card()
                
    def exists(self, student_name):
        for student in self.students:
            if student_name == student.name:
                return True
            return False
        
    def add_mark(self, student_name, subject, mark):
        for student in self.students:
            if student_name == student.name:
                return student.add_mark(subject, mark)
            return "Student not found"
        
    