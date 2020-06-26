## Determine half-life of Carbon-14.
amount = 1
years = 0
while amount >= .5:
    amount -= .00012 * amount
    years += 1
print("Carbon-14 has a half-life")
print("of", years, "years.")
