## Make change for an amount of less than one dollar.
amount = int(input("Enter amount of change: "))
remainder = amount
quarters = remainder // 25
remainder %= 25
dimes = remainder // 10
remainder %= 10
nickels = remainder // 5
remainder %= 5
cents = remainder
print("Quarters:", quarters, end="   ")
print("\tDimes:", dimes)
print("Nickels:", nickels, end="   ")
print("\tCents:", cents)
