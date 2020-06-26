## Calculate cost of electricity.
wattage = int(input("Enter wattage: "))
hoursUsed = float(input("Enter number of hours used: "))               
price = float(input("Enter price per kWh in cents: "))                
cost = (wattage * hoursUsed) / (1000 * price)
print("Cost of electricity:", '$' + str(round(cost, 2)))
