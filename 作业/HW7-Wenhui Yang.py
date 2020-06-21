"""
## HW7: Exception Handing
## HW7-Wenhui Yang
## Wenhui Yang
## 4/29/2019
"""

def main():
    aDict = createDictionary("EuropeByPop.txt") 
    for k in aDict:
        aDict[k] = eval(aDict[k])     
    titleDict = {}
    for k in aDict:   
        v = aDict[k]  
        titleDict.update({k.title():v})
    print(aDict)
    while True:
        try:
            nation = (input("Enter a country in Europe for its population: ")).title()
            print(aDict[nation])
            break
        except KeyError:
            print("Unacceptable nation was entered.")  
    print('-' * 60)
    print(nation)
    getPop(nation, titleDict)
    displayStats(aDict)

"""
Name:      createDictionary
Purpose:   To create a dictionary data structure from a text file
Parameter: a text file - string
Return:    a dictionary
"""  
                   
def createDictionary(fileName):
    try:
        infile = open(fileName, 'r')
        textList = [line.rstrip() for line in infile]
        infile.close()
    except IOError:
        print("Error: cannot find or read data")
    else:
        print("the file opened successfully")
        return dict([x.split(',') for x in textList])

"""
Name:      getPop
Purpose:   To retrieve a population associated with a country
Parameter: a string, a dictionary
Return:    None
"""  
      
def getPop(nation, aDict):
    try:
        print("The population of " + nation + " in millions is", aDict.get(nation, "Check your spelling!"))
    except Exception as exp:
        print("Error",exp.args)
        
"""
Name:      calcMedian
Purpose:   To calculate the median of values in a dictionary  
Parameter: object - a dict_values object
Return:    float - the median
"""

def calcMedian(aList):
    try:
        aList = list(aList)
        count=len(aList)
        n = int(count/2)
        if count%2==0:
            median=(aList[n - 1] + aList[n]) / 2
        else:
            median=aList[n]
    except Exception as exp:
        print("Error",exp.args)
    finally:
        return median


"""
Name:      displayStats
Purpose:   To display various statistical results    
Parameter: a Dictionary
Return:    None
"""

def displayStats(aDict):
    try:
        mean = sum(aDict.values())/len(aDict)
        valueList = aDict.values()
        median = calcMedian(valueList)
    except Exception as exp:
        print("Error",exp.args)
    finally:
        print('-' * 60)
        print("The average population of Europe in millions is:"
              " {:,.2f}".format(mean), "and the median" \
              " population in millions is:", median)
    
    
main()    


