import pickle
from nation import Nation

def main():
    ## Display information about a country.
    nationDict = pickle.load(open("nationDict.dat", "rb"))
    country = input("Enter a country: ")
    print("Continent:", nationDict[country].getContinent())
    print("Population: {0:,.0f}".
          format(1000000 * nationDict[country].getPopulation()))
    print("Area: {0:,.2f} square miles".
          format(nationDict[country].getArea()))

main()

