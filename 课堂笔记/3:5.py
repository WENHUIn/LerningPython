#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 09:55:10 2019

@author: ninenins
"""

# for loop has range(start stop,step)
# defualt (0,step,1) 

## compare the while and for loops
#########################################
print("The while loop results")
n = 0
while n < 5:
    print(n)
    n += 1
## the for loop
print("The for loop results")
for m in range (5):
    print(m)
    
## loop through a tuple
months = ("January","February","March","April","Octorber","December")
for item in months:
    if "r" in item.lower():
        print(item)
 ## the outer loop  
for m in range(1,6):
    ## the inner loop
    for n in range (1,6):
        print(m, "x", n, "=", m*n, "\t",end=" ")
        
## show how to create a list by reading a file of strings
## using a for loop
dataList = []

infile = open("/Users/ninenins/Desktop/python/课本/DataFile.txt","r")

for line in infile:
    dataList.append(line.strip())
infile.close()

print(dataList)
        























 




