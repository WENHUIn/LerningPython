## Newton's Law of Cooling.
temperature = 212
count = 0
while temperature > 150:
    count += 1
    temperature -= (temperature - 70) * 0.079
print("The coffee will cool to below")
print("150 degrees in", count, "minutes.")  

