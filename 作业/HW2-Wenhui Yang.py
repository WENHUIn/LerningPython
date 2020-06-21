#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# HW2-String formatting
# Wenhui Yang
# 2/10/2019
"""
SPY = eval(input("Please enter the amount invested in SPY : "))
QQQ = eval(input("Please enter the amount invested in QQQ : "))
EEM = eval(input("Please enter the amount invested in EEM : "))
VXX = eval(input("Please enter the amount invested in VXX : "))
totalamount = (SPY + QQQ + EEM + VXX)

print("Enter amount invested in SPY:" + str(SPY))
print("Enter amount invested in QQQ:" + str(QQQ))
print("Enter amount invested in EEM:" + str(EEM))
print("Enter amount invested in VXX:" + str(VXX))

print("ETF\tPERCENTAGE\t")
print("------------------")

form = " {0:s}      {1:.2%} "
print(form.format("SPY", SPY / totalamount))
print(form.format("QQQ", QQQ / totalamount))
print(form.format("EEM", EEM / totalamount))
print(form.format("VXX", VXX / totalamount))
print("TOTAL AMOUNT INVESTED: " + "$" + str(totalamount))

