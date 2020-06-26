import point

def main():
    ## Determine the distance of a point from the origin.
    x = float(input("Enter the x-coordinate of point: "))
    y = float(input("Enter the y-coordinate of point: "))
    p = point.Point(x, y)
    print("Distance from origin: {0:,.2f}".
          format(p.distanceFromOrigin()))

main()

#### point.py
##class Point:
##    def __init__(self, x, y):
##        self._x = x
##        self._y = y
##        
##    def distanceFromOrigin(self):
##        return (self._x ** 2 + self._y ** 2) ** .5

                                      
    
