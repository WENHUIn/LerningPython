class Nation:
    
    def __init__(self):
        
        self_name = ""
        self_continent = ""
        self_population = 0.0
        self_area = 0

    def setName(self, name):
        self._name = name
    def getName(self):
        return self._name

    def setContinent(self, continent):
        self._continent = continent
    def getContinent(self):
        return self._continent

    def setPopulation(self, population):
        self._population = population
    def getPopulation(self):
        return self._population

    def setArea(self, area):
        self._area = area
    def getArea(self):
        return self._area

    def popDensity(self):
        return self._population / self._area
    
