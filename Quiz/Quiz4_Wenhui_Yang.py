"""
## Quiz4-functions
## Quiz4_Wenhui_Yang.py
## Wenhui Yang
## 4/4/2019
"""
#1
def main():
    writetxt()
    skPrice = extractfield("quiz4_data.txt",3)
    prices = [eval(item) for item in skPrice]
    display(prices)
    
def writetxt():
    outfile = open("quiz4_data.txt","w")
    outfile.write("Apple,23.84%,195.36\n")
    outfile.write("Citigroup,24.97%,65.06\n")
    outfile.write("Google,15.87%,1210.81\n")
    outfile.write("Microsoft,18.12%,119.99\n")
    outfile.close()

def extractfield(fileName,n):
    infile = open(fileName,"r")
    return [line.rstrip().split(",")[n-1] for line in infile] 
  
def calcmedian(listName):
    listName.sort()
    n = len(listName)
    if (n % 2 != 0):
        median = listName[int(n/2)]
    else:
        median = ((listName[int(n/2)] + listName[int(n/2)-1])) / 2
    return median

def display(listName):
    avgskprice = sum(listName)/len(listName)
    medianprice = calcmedian(listName)
    print("The average stock price is: ${0:.2f}".format(avgskprice))
    print("The median stock price is: ${0:.2f}".format(medianprice))
    
main()


