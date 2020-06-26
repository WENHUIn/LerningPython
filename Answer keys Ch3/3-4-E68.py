## Calculate value of stock at end of year.
value = 10000
for i in range(6):
    value -= .16 * value
for i in range(6):
    value += .18 * value
print("The value of the stock at the")
print("end of the year was ${0:,.2f}.".format(value))





  

