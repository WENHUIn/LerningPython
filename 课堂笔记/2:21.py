#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 10:03:33 2019

@author: ninenins
"""

areas = [("NE",55.3,234.3)\
         ("NW",66.9,566.4)\
         ("S",114.6,300.9)\
         ("W",71.9,678.2)]

## using compoud conditions
state = input("Enter your state: ")
if (state == "CT") or (state == "NY") or (state == "MD"):
    print("I found you")
else:
    print("Not there")
 
## simplify by using tuple
city = input("enter city: ")
if city in ("Rome","NYC","LA","SF"):
    print("Great place")
else:
    print("Oh!NO!")
    
## simplify by using list
country = input("Enter country: ")
if country in ["USA","UK","CN","JPN"]:
    print("I have been there")
else:
    print("want to visit")
    
print("I shouldn't be here")
  
## determine the larger of the two numbers
num1 = eval(input("Enter the first number: "))
num2 = eval(input("Enter the second number: "))
lgValue = num1
if (num1 > num2):
    lgValue = num1
elif (num1 < num2):
    lgValue = num2
else:
    print("Two numbers are equal")
    
print("The larger value is",str(lgValue) + ".")

## nested if 
num1 = eval(input("Enter the first number: "))
num2 = eval(input("Enter the second number: "))
if (num1 >= num2):
    if (num1 == num2):
        print("Two numbers are equal")
    else:
        lgValue = num1
else:
    lgValue = num2

print("The larger value is",str(lgValue) + ".")
    
first = eval(input("Enter the first number: "))
second = eval(input("Enter the sencond number: "))
third = eval(input("Enter the third number: "))
maxnumber = first
if (second > first):
    maxnumber = second
else: maxnumber = first
if (third > second):
    maxnumber = third
else: maxnumber = first
str(maxnumber)
print("The largest number is: " + str(maxnumber) + ".")

color = input("color: ")
status = input("status: ")
if (color == "blue"):
    if status == "steady":
        print("clear view")
    else:
        print("clouds due")
else:
    if status == "steady":
        print("rain ahead")
    else:
        print("snow instead")
        
    
costs = eval(input("costs: "))
revenue = eval(input("revenue: "))
if costs == revenue:
    print("Break even")
else:
    if costs > revenue:
        loss = costs - revenue
        print("The loss is : " + str(loss))
    else:
        profit = revenue - costs
        print("The profit is :" + str(profit))
    
    
x = eval(input("score: "))
if not(0 <= x <= 100):
        x = eval(input("Please input your score, which is between 0 and 100: "))
        if x >= 90:
            G = "A"
        elif (80 <= x < 90):
            G = "B"
        elif (70 <= x < 80):
            G = "C"
        elif (60 <= x < 70):     
            G = "D"
        else:
            G = "F"
else:
    if (x >= 90):
        G = "A"
    elif (80 <= x < 90):
        G = "B"
    elif (70 <= x < 80):  
        G = "C"
    elif (60 <= x < 70):     
        G = "D"
    else:
        G = "F"
print("Your grade is: " + G)

    






























   
