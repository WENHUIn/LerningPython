class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y
    def distanceFromOrigin(self):
        return (self._x ** 2 + self._y ** 2) ** .5
