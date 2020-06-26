## Determine amount of radioactive material remaining.
amount = 10
for i in range(5):
    amount *= .88
print("The amount of cobalt-60 remaining")
print("after five years is {0:.2f} grams.".format(amount))
