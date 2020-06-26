## Display the effects of supply and demand.
print("YEAR   QUANTITY    PRICE")
quantity = 80
price = 20 - (.1 * quantity)
print("{0:d}     {1:.2f}     ${2:.2f}".format(2014, quantity, price))
for i in range(4):
    quantity = 5 * price - 10
    price = 20 - (.1 * quantity)
    print("{0:d}     {1:.2f}     ${2:.2f}".format(i + 2015, quantity, price))
