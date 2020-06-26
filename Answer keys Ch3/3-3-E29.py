## Determine when India's population will surpass China's population.
chinaPop = 1.37
indiaPop = 1.26
year = 2014
while indiaPop < chinaPop:
    year += 1
    chinaPop *= 1.0051
    indiaPop *= 1.0135
print("India's population will exceed China's")
print("population in the year", str(year) + '.')
