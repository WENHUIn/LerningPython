## Determine when Consumer Price Index will double.
cpiIn2014 = 238.35
cpi = cpiIn2014
years = 0
while cpi <=  2 * cpiIn2014:
    cpi = 1.025 * cpi
    years += 1
print("Consumer prices will")
print("double in", years, "years.")
