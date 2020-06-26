## Drop a ball and find number of bounces and total distance traveled.
coefOfRestitution = float(input("Enter coefficient of restitution: "))
height = float(input("Enter initial height in meters: "))

height *= 100   # convert to centimeters
distanceTraveled = 0
bounces = 1     # first bounce
distanceTraveled = height
while height * coefOfRestitution >= 10:
    bounces += 1
    height = coefOfRestitution * height
    distanceTraveled += 2 * height  # up then down again
distanceTraveled /= 100             # convert back to meters    
print("Number if bounces:", bounces)
print("Meters traveled: {0:,.2f}".format(distanceTraveled))
