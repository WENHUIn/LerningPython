#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# display left and right digits
# Quiz1_Wenhui_Yang
# Wenhui Yang
# 1/31/2019
"""
"""
更新于2020/6/20 想想当初的自己还真是有点蠢鸭哈哈哈
"""
#%%
#generate a number
x = str(eval(input("Enter a number: ")))
#print 3 digits to the left of decimal point
decimal = x.rfind('.')
print ("left 3 digits: " + x[decimal-3:decimal])
#print 2 digits to the right of decimal point 
print ("right 3 digits: "+ x[decimal+1:decimal+3])

"""
# replace a word
# Quiz1_Wenhui_Yang
# Wenhui Yang
# 1/31/2019
"""
#%%
#generate a sentence
sentence = input("enter a sentence")
sl = sentence.split(' ')
sl[0] = "who"
newsent = (' ').join(sl)
print(newsent)
