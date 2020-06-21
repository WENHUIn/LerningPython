#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 09:35:56 2019

@author: ninenins
"""


s1 = "abcd"
slength = len(s1)
s1Upper = s1.upper()
s1Upper

s1 = "abcdcc"  #count the number
s1count = s1.count("c")

aBook = "moby Dick"
print (aBook.title()) #titile you only make the first letter capital
print(aBook.capitalize(),aBook.upper(),aBook.lower())

bookLen = len(aBook)
print (bookLen)
print (len(aBook))

print (aBook.count("M"))

print("The number of characters for this book is :" + str(bookLen))
#make it string

\n
\t
\"
\\

print("The number of \"M\" is: " + str(aBook.count("M")))
fullName = input("Please input your full name :")
print(fullName)




























