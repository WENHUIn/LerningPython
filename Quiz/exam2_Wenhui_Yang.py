"""
## Program: Exam2
## File name: Exam2_Wenhui_Yang
## Author: Wenhui Yang
## Data: 5/2/2019
"""
def main():
    try:
        teams = createList("Peachbowl.txt")
        Dict = createDict(teams)
        displayTopTen(Dict)
    except Exception as exp:
        print("Error: in main()",exp)
        
def createList(fileName):
    try:
        infile = open(fileName,"r")
        peachbowl = [line.rstrip() for line in infile]
        infile.close()
    except FileNotFoundError:
        print("The file cannot access.")
    else:
        return peachbowl
        print("The file opend.")

def createDict(listName):
    try:
        freqDict = {}
        for team in listName:
            freqDict[team] = 0
        for team in listName:
            freqDict[team] += 1
    except Exception as exc:
        print("Error: in createDict(listName)",exc)
    else:    
        return freqDict

def displayTopTen(aDict):
    try:
        print("Teams with five or more " + \
              "Peach Bowl wins as of 2015")
        list5 = []
        for team in aDict.keys():
            if aDict[team] >= 5:
                list5.append((team,aDict[team]))
        list5.sort(key = lambda x:x[1], reverse = True)
        for item in list5:
            print("{0:s} : {1:d}".format(item[0],item[1]))
    except Exception as exp:
        print("Error: in displayTopTen(aDict)",exp)
        
main()        
        
        
        
        
        