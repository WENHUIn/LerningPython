#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 09:34:10 2019

@author: ninenins
"""

function 
- /w 
- w/o 
- natural statement
- w/o 
#1.define
#2.invoke or call
str1.lower()

def is_even(i):
    """
    Input: i, a positive in
    Returns True if i is even , otherwise False
    """
    print("inside is_even")
    return i%2 == 0
is_even(3)

"""formal parameter gets bound to the value of actual parameter 
when function is called"""

def f(x):
    x = x + 1
    print("in f(x): x = ", x)
    return x

x = 3
z = f(x)


## define a main fn as a starting point of a program


##############################################################################
## a fn has multiple parameters
def presentValue(f,r,n):
    """
    f - future value
    r - annual rate of interest in decimal form
    n - the number of the years
    """
    pValue = f/((1 + (r/100)) ** n)
    return pValue 

def main1():  # make it ready to call presentValue()
    f1,r1,n1 = getInput() ## use tuple or single argument
    print("Present value: ${0:,.2f}".format(presentValue(f1,r1,n1)))
    
def getInput():
    f1 = eval(input("Enter the future value: "))
    r1= eval(input("Enter the interest rate (as %): "))
    n1 = eval(input("Enter the number of years: "))
    return f1,r1,n1
main1()
##############################################################################
## this fn has no parameter nor return value
def main():
    ## invoke fns had been defined her
    print(getFirstName())
    tempC = eval(input("Enter a temperature in Celsius degree: "))
    print("The F equivalent: ", toFahrenheit(tempC),"degrees")
##############################################################################
## Fn example
## a function with no parameter
def getFirstName():
    """
    
    """
    fName = input("Enter your first name: ")
    return fName
getFirstName()

##############################################################################
## a fun has 1 parameter
def toCelsius(temp):
    ## convert Fahrenheit temp to Celsius
    resultTemp = (5/9) * (temp -32)
    return resultTemp
toCelsius(90)

def toFahrenheit(temp):
    ## convert Celsius temp to Fahrenheit  
    return temp * (9/5) + 32
toFahrenheit(23)

##############################################################################
































