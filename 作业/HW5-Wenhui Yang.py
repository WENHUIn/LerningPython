#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# HW5
# functions
# Wenhui Yang
# 3/30/2019
"""

## 1
def calcmm(P,r,n):
    M = (P*r*(1+r)**n) / ((1+r)**n - 1)
    return(M)

def main():
    P = eval(input("Enter your principal: "))
    R = eval(input("Enter your annual rate: "))
    r = R/1200
    n = eval(input("Enter the months of payment: "))
    print("Your principal is {0:.2f}".format(P))
    print("Your monthly rate is {0:.2f}".format(r))
    print("Your payment of month(s) is {0:}".format(n))
    print("Your monthly payment is {0:.2f}".format(calcmm(P,r,n)))
main()

print("-"*30)
## 2
def txt():
   f = open("planets.txt","w")
   f.write("Mercury\nVenus\nMars\nEarth\nJupiter\nNeptune\nSaturn\nUranus")
   f.close()

def readtxt():
    txt()
    infile = open("planets.txt","r")
    dataList = []
    for line in infile:
        dataList.append(line.strip())
    infile.close()
    newlist = dataList.sort()
    newlist = dataList[0:5]
    print("The first five planets are: " + str(newlist))
readtxt()
    
        
