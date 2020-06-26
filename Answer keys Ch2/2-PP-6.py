
## Convert a measurement from miles, yards, feet,
## and inches, to a metric one in meters, kilometers,
## and centimeters.
miles = float(input("Enter number of miles: "))
yards = float(input("Enter number of yards: "))
feet = float(input("Enter number of feet: "))
inches = float(input("Enter number of inches: "))
# Step #1: Add up given measurements into inches
totalInches = inches + 12 * feet + 36 * yards + 63360 * miles
# Step #2: Convert total inches into total meters
totalMeters = totalInches / 39.3700787  
# Step #3: Compute kilometers, whole meters, and centimeters
# Step 3a: compute # of kilometers, subtract from meters
kilometers = int(totalMeters / 1000)
totalMeters = totalMeters - 1000 * kilometers
meters = int(totalMeters)
centimeters = 100 * (totalMeters - meters)
centimeters = round(centimeters, 1)
print("Metric length:")
print(" ", kilometers, "kilometers")
print(" ", meters, "meters")
print(" ", centimeters, "centimeters")


