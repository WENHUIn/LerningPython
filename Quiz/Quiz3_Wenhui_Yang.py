#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# Quiz3
# if else elif
# Wenhui Yang
# 2/28/2019
"""

## Question 1
a = eval(input("Please enter a: "))
b = eval(input("Please enter b: "))
c = eval(input("Please enter c: "))
condition = b**2 - 4*a*c
solution1 = (-b + (b**2 - 4*a*c)**0.5) / 2*a
solution2 = (-b - (b**2 - 4*a*c)**0.5) / 2*a
if a == 0:
    a = eval(input("Please enter a, which is not equal to 0 : "))
    if condition >= 0:
        if condition > 0:
            print("Solutions are {0:.2f}  and {1:.2f}".format(solution1,solution2))
        else:
            print("Solutions are euqual, they are {0:.2f}".format(solution1))
    else:
        print("None solutions")
else:
    if condition >= 0:
        if condition > 0:
            print("Solutions are {0:.2f}  and {1:.2f}".format(solution1,solution2))
        else:
            print("Solutions are equal, they are {0:.2f}".format(solution1))
    else:
        print("None solutions")

## Question 2
year = int(input("Please enter a year: "))
if (year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0)):
    print(str(year) + " is a leap year.")
else:
    print(str(year) + " is  not a leap year.")
        
    
    
        
