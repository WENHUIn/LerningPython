#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# Quiz2
# About string format
# Wenhui Yang
# 2/14/2019
"""

# Qestion 1
number = input("Please enter your phone number: ")
lnumber = list(number)
lnumber.insert(3,"-")
lnumber.insert(7,"-")
snumber = "".join(lnumber)
print(snumber)


# Qestion 2
print("01234567890123456789012345")
print("{0:^5s}{1:<17s}{2:>4s}".format("Order","Owner","Cost"))
print("{0:^5s}{1:<17s}{2:>4s}".format("1","Mae Terry","87"))
print("{0:^5s}{1:<17s}{2:>4s}".format("2","Hay John","234"))
print("{0:^5s}{1:<17s}{2:>4s}".format("3","Lee Don","103"))