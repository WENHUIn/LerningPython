# -*- coding: utf-8 -*-
#HW6 solution:
# 
# use whole dictionary for the whole thing
## clear default message
## change key use title
# create the new dictionary: titleDict={}
##  hush number immutable
## give user back 
## when do the calsMedian, pass the dictionary, dictionary are object associate the key not number not support index, key do not associated index: aList = list(aList) 
## you should change dictionary into list, not really index when do mean
## check your spelling not in European countries
## use module package it is easy to use

## try some dictionary functions/operations
## put everything in main

def main():
    #dict is the key word
    ditn = {} #declare the dictionary
    ## pass the variable in the dictionary
    ditn["apple"] = 3 # add in item to it 
    print(ditn)
    #modify value of apple add another item
    ditn.update({"apple":1, "banana":2})
    ## use the len fct
    print("ditn has", len(ditn), "items")
    print(ditn)
    ## how code operate follow the order
    ##3 check if an item is in the ditn
    #print("banana" in ditn) # key in dictionary 
    ## add two more item 
    ditn["cherry"] = 3
    ditn["pear"] = 2
    # print the list of key in it
    print("keys:", list(ditn.keys()))
    # print list of value
    print("values:", list(ditn.values())) ## if not used.value use loope, value can be duplicate builtin_function_or_method' object is not iterable
    # print the entire dict
    for key in ditn:
        print(key, ditn[key])
    # check if an item is in it
    print(ditn.get("orange", "this item is not in dictionary"))
    print(ditn.get("apple", "this item is in dictionary"))

    # create a new one
    ditn2 = {}
    # copy the 1st to the 2nd 
    ditn2 = dict(ditn)
    ## delete an item from the ditn2
    del ditn2["banana"]
    # modify ditn2
    ditn2.update({"orange":5, "kiwi":4, "pear":7}) # change the pear
    print(ditn2)
    ## merge new one wins, later one always wins
    ## merge two ditns
    ditn.update(ditn2)     ## dupliacte higher poriority will replacate other one 
    ## duplicates will be replaced with the one in ()
    print("dictionary after merging.", ditn)
    
main()

#********* frquency count the duplicate comma ***********#

## create a list of words from the text file
def formListOfWords(fileName):
    infile = open(fileName)                  # there aren't newline characters to get rid of 
    originalLine = infile.readline().lower() # lowercase
    line = ""                                # create a new line
    for ch in originalLine:                  # [[loop through original line to put each
        if ("a" <= ch <= "z") or (ch == " "):# individual line onto a line]]
            line += ch
    listOfWords = line.split()               # put each word onto a list and return if 
    return listOfWords

def createFreqDict(aWordList):
    freqDitn = {}
    for word in aWordList:
        freqDitn[word] = 0     #[[initialize the word freq dict, 
    for word in aWordList:     #so each word has 0 frequece firstly]]
        freqDitn[word] += 1    #add the freq to the word
    return freqDitn             






