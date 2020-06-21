"""
## Exception Handling
## 4/25/2019
"""
## catch specific type of exception
def main():
    EuDitn = createDictionary("EuropeByPop.txt")
    writeFile(EuDitn,"Sample.txt")
    getInput()
    
def getInput():
    aDitn = {"a":"alpha","b":"bravo","c":"charlie"}
    while True:
        try:
            letter = input("Enter a, b, or c: ")
            print(aDitn[letter])
            break
        except KeyError:
            print("Unacceptable character was entered.")

## catch specific type of exception and use else clause
def createDictionary(fileName):
    try:
        infile = open(fileName,"r")
        textList = [line.rstrip() for line in infile]
        infile.close()
    except IOError:
        print("Error: cannot find or read data")
    else:
        print("the file opened successfully")
        return dict([x.split(",") for x in textList]) # dict([list])

## catch unspecific type of exception and use finally clause
def writeFile(aDitn,fileName):
    try:
        outfile = open(fileName,"w")
        for key in aDitn:
            outfile.write(key + "\n")
    except Exception as exp:
        print("Error: in writeFile(fileName)",exp.args)
    finally:
        print("got here")
        outfile.close()
            
main()            

import os            
os.chdir("/Users/ninenins/Desktop/python/File")
            
            
            
            
            
            
            
            
            
            