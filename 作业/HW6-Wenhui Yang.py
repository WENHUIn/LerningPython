
"""
## HW6:Dictionary
## HW6-Wenhui Yang
## Wenhui Yang
## 4/13/2019
"""
def main():
    Europedict = createDict("EuropeByPop.txt")
    EuropeasStrings = extractField("EuropeByPop.txt",2)
    pop = [eval(pop) for pop in EuropeasStrings]
    allcountry = countryname("EuropeByPop.txt")
    display(pop)
    print("-"*50)
    print("Please enter a country's name to get its population.")
    country = input("Country: ")
    while country not in allcountry:
        country = input("Error, please try again: ")
    print("The country has population: ",Europedict[country],"millions.")

def extractField(fileName,n):
    infile = open(fileName,"r")
    return [line.rstrip().split(",")[n-1] for line in infile]

def countryname(fileName):
    infile = open(fileName,"r")
    return [line.rstrip().split(",")[0] for line in infile]

def display(listofpop):
    avgpop = sum(listofpop)/len(listofpop)
    medianpop = calcMedian(listofpop)
    print("The average population is: {0:.2f} millions".format(avgpop))
    print("The median population is: {0:.2f} millions".format(medianpop))
    
def calcMedian(listofpop):
    if len(listofpop)%2==1:
        median = listofpop[int(len(listofpop)/2)]
    else:
        n = int(len(listofpop)/2)
        median = (listofpop[m] + listofpop[m-1])/2
    return median

def createDict(fileName):
    infile = open(fileName,"r")
    textList = [line.rstrip() for line in infile]
    infile.close()
    return dict([country.split(',') for country in textList])

main()

        
