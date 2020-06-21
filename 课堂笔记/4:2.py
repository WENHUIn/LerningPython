"""
## Name: usingCSVpy
## Purpose: To practice how to analyze data
## Author: book example
## Date: 4/2/2019
"""
import os
os.chdir("/Users/ninenins/Desktop/python/File")

def main():
    ## place prices into a list
    skPrice = extractField("DOW_Stocks.txt",4)
    ## The prices in the list are in string format, convert them 
    prices = [eval(item) for item in skPrice]
    ## The yield in 3rd field can be extracted and also remove & sign
    skYield = extractField("DOW_Stocks.txt",3)
    yields = [item.rstrip("%") for item in skYield]
    ## Check if "%" is gone
    print(yields)
    displayStates(prices)
## a fn to extract data from file
"""
purpose: extract the nth field from each record of a csv file
parameter: a file (CSV or txt format)
return: a list of nth field from each record
"""
def extractField(fileName,n):
    infile = open(fileName,"r")
    return [line.rstrip().split(",")[n-1] for line in infile] #list

def calcMedian(listName):
    listName.sort()
    lenlist = len(listName)
    if (lenlist % 2 != 0):
        median = listName[int(len(listName)/2)]
    else:
        median = sum(listName[int(len(listName)/2)] + 
                              listName[int(len(listName)/2 -1)])/2
    return median

## display statistics
def displayStates(listName):
    mean = sum(listName)/len(listName)
    median = calcMedian(listName)
    sd = calcSD(listName,mean)
    print("average price: ${0:.2f}".format(mean))
    print("median is: ${0:.2f}".format(median))
    print("standard deviation is: ${0:.2f}".format(sd))

"""
parameters: a list
return: the median
"""
def calcMedian(listName):
    listName.sort()
    lenlist = len(listName)
    if (lenlist % 2 != 0):
        median = listName[int(len(listName)/2)]
    else:
        median = sum(listName[len(listName)/2] + listName[len(listName)/2 -1])/2
    return median

def calcSD(listName,mean):
    n = len(listName)
    ## create an n elements list with value 0
    listSqDev = [0]*n
    ## get each distance of data point from the mean
    for i in range(n):
        listSqDev[i] = (listName[i] - mean) ** 2 
    sd = (sum(listSqDev)/n)** 0.5
    return sd

main()

        
    
    





























