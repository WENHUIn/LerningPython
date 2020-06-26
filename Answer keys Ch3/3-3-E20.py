## Determine the year that the world population will exceed
## 8 billion, assuming a 1.1% rate of increase.
yr = 2011       # start at 2011
pop = 7         # population of 7 billion
while pop <= 8:
    pop = (1.011) * pop
    yr += 1
print("World population will be \n8 billion in the year", str(yr) + ".")
