## Determine value of an increasing annuity.
months = 0
balance = 0
while balance <= 3000:
    balance = (1.0025 * balance) + 100
    months += 1
print("Annuity will be worth")
print("$3000 after", months, "months.")
