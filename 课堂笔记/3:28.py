#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
## functions:part2
## 4/2/2019
"""

## write()
## writeline()  list or tuple

## create a file containing some cartoon characters
def main():
    outfile = open("Cartoon.txt","w")
    useWrite(outfile)
    add("Cartoon.txt")
    print("Check if file is created.")     
def useWrite(outfile):
    outfile.write("Bugs Bunny\n")
    outfile.write("Daffy Duck\n")
    outfile.write("Minnie Mouse\n")
    outfile.close()
def add(fileName):
    outfile = open(fileName,"a") ## "a" --- append
    outfile.write("Pigs Porky\n")
    ## add one more line with new data 
    listNew = ["Brown Charlie\n","Bear Yogi\n"] 
    outfile.writelines(listNew)
    outfile.close()

main()

infile = open("NumberFile.txt","r")
datalist = [eval(line) for line in infile]
infile.close()






    