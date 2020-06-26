def main():
    ## Determine the distance between two points.
    x1 = float(input("Enter x-coordinate of first point: "))
    y1 = float(input("Enter y-coordinate of first point: "))
    x2 = float(input("Enter x-coordinate of second point: "))
    y2 = float(input("Enter y-coordinate of second point: "))
    p = Point(x1 - x2, y1 - y2)
    print("Distance between points: {0:,.2f}".format(p.distanceFromOrigin()))

class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y
        
    def distanceFromOrigin(self):
        return (self._x ** 2 + self._y ** 2) ** .5

main()

                                      
    
