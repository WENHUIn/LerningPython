## Determine the unit price of a purchase.
price = float(input("Enter price of item: "))
print("Enter weight of item in pounds and ounces separately.")
pounds = float(input("Enter pounds: "))
ounces = float(input("Enter ounces: "))
weightInOunces = 16 * pounds + ounces
pricePerOunce = price / weightInOunces
print("Price per ounce: ${0:.2f}".format(pricePerOunce))
