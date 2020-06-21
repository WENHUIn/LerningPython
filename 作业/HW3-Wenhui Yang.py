#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# HW3
# if elif else
# Wenhui Yang
# 2/22/2019
"""
#######################################
# Question 1

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

#######################################
# Question 2

word = input("Please enter a word: ")
word = word.lower()    
lword = list(word)
vowel = ["a","e","i","o","u"]
if lword[0] in vowel:
    lword.insert(len(lword),"way")
    nword = "".join(lword)
    print("Pig Latin is " + nword + ".")
else:
    wherevowel = []
    if 'a' in word:
        wherevowel.append(word.find('a'))
    if 'e' in word:
        wherevowel.append(word.find('e'))
    if 'i' in word:
        wherevowel.append(word.find('i'))       
    if 'o' in word:
        wherevowel.append(word.find('o'))
    if 'u' in word:
        wherevowel.append(word.find('u'))   
    wherevowel = min(wherevowel)
    word = word[wherevowel:] + word[:wherevowel] + "ay"
    print("Pig Latin is " + word + ".")


    
      
       

























