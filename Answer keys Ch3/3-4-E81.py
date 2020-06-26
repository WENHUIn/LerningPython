## Calculate number of odometer readings containing the digit 1.
total = 0
for n in range(1000000):
    if '1' in str(n):
        total += 1
print("{0:,d} numbers on the odometer".format(total))
print("contain the digit 1.")
