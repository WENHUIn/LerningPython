#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
## HW4:loop,define functions
## Wenhui Yang
## 3/10/2019
"""
######################################
## Question1

scorelist = []
score = eval(input("Please enter your scores: "))
while True:
    if not (0<= score <= 100):
        score = eval(input("Please enter your scores again: "))
    else:
        scorelist.append(score)
        if len(scorelist) == 6:
            break
        score = eval(input("Please enter your scores: "))   
scorelist.sort()
scorelist = scorelist[1:]
averagescore = sum(scorelist)/len(scorelist)
print("The averagescore is: " + str(averagescore))

x = averagescore
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
print("Your grade is: " + G)

################################
print("######################################")
## Question2
 
def describe():
    print("This program displays a person's")
    print("name and next year's salary.")
    
def getname():
    fname = input("Enter your first name: ")
    lname = input("Enter your last name: ")
    name = fname + " " + lname
    return name

def currentsalary():
    salary = eval(input("Enter your current salary: "))
    return salary
    
def calculatesalary(salary):
    if salary >= 50000:
        nextsalary = salary + 3000 + (salary - 50000)*0.015
    else:
        nextsalary = salary * 1.03
    return nextsalary

def Output(name,nextsalary):
    print("{0:s} next year will have salary:${1:,.2f}"
          .format(name,nextsalary))

def main():
    describe()
    name = getname()
    salary = currentsalary()
    nextsalary = calculatesalary(salary)
    Output(name,nextsalary)

main()
    




















