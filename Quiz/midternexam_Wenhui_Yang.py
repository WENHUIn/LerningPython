#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
## Exam1
## Wenhui Yang
## 3/14/2019
"""
def calSum():
    totalsum = 0
    i = 2
    while (i <= 88):
        if i%2 == 0:
            totalsum += i
    print(totalsum)
    
def findPower(x,n):
    product = x**n
    return(product)

def calPay(cost,taxRate,tipRate):
    total = cost*(taxRate/100) + cost*(tipRate/100) + cost
    return(total)

def selectMenu():
    print("1.Calculate a sum of even intergers between 2 and 88,inclusive")
    print("2.Calculate a value x raised to the power of n ")
    print("3.Calculate the final payment for a meal consumed in a restaurant")
    print("4. Quit")
    while True:
        num = int(input("Make a selection from the menu: "))
        if num == 1:
            thenumber = calSum()
            print(thenumber)
        elif num == 2:
            x = eval(input("Enter x: "))
            n = eval(input("Enter n: "))
            product = findPower(x,n)
            print("The final product is: " + str(product))
        elif num == 3:
            cost = eval(input("Please enter your cost: "))
            taxRate = eval(input("Please enter the taxrate: "))
            tipRate = eval(input("Please enter the tiprate: "))
            pay = calcPay(cost,taxRate,tipRate)
            print("You need to pay $: {0:.2f}".format(pay))
        elif num == 4:
            break

def main():
    calcSum()
    findPower(x,n)
    calPay(cost,taxRate,tipRate)
    selectMenu()

main()
        
            
                    
            
            
            
            
            
            
            
            
            