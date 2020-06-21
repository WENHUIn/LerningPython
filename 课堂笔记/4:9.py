"""
find sd
CSV
lambda expression
dictionary
"""
## lambda part1,part2,...:expression
## lambda fn usague 4.2 example 7
def Main():
    names = ["Den Ritchie","Alan Kay","John D. Backus","James F. Gosling"]
    ## sort the items based on the last group of a string separated by space
    names.sort(key = lambda name: name.split()[-1])
    nameString = ",".join(names)
    print(nameString)
Main()
    
## Dictionary
def translate(color):
    if color == "red":
        return "aka"
    elif color == "blue":
        return "ao"
    elif color == "green":
        return "midori"
    elif color == "white":
        return "shiro"
## use dictionary
translate = {"red":"aka","blue":"ao","green":"midori","white":"shiro"}
translate["red"]
translate["green"]
    
    
    
    
    
    
    
    
    
import os
os.getcwd()
os.chdir("/Users/ninenins/Desktop/python/File")