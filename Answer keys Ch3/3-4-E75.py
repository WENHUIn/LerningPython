## Calculate probabilities that at least two  
## people in a group have the same birthday.
print("{0:17} {1}".format("NUMBER OF PEOPLE", "PROBABILITY"))
# r = size of group
for r in range(21, 26):
    product = 1
    for t in range(1, r):
        product *= ((365 - t) / 365)
    print("{0:<17} {1:.3f}".format(r, 1 - product))
