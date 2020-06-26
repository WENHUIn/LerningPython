import pickle
from nation import Nation

def main():
    ## Display the most density populated countries on a continent.
    nationDict = pickle.load(open("nationDict.dat", "rb"))
    nationList = list(nationDict.keys())
    continent = input("Enter a continent: ")
    nationsInContinent = [nation for nation in nationList if
             nationDict[nation].getContinent() == continent]
    nationsInContinent.sort(key=lambda x: nationDict[x].popDensity(),
                            reverse=True)
    for i in range(5):
        print(nationsInContinent[i])

main()

