class Circle:
    def __init__(self, radius=1):
        self._radius = radius
    def setRadius(self, radius):
        self._radius = radius
    def getRadius(self):
        return self._radius
    def area(self):
        return 3.14 * self._radius * self._radius
    def circumference(self):
        return 2 * 3.14 * self._radius
