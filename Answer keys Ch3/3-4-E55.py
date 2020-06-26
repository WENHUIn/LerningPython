## Total the fractions 1/n for n = 1 through 100.
sum = 0
for i in range(1, 101):
    sum += 1 / i
print("The sum of 1 + 1/2 + 1/3 + ... + 1/100")
print("is {0:.5f} to five decimal places.".format(sum))

