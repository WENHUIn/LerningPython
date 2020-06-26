## Compare simple interest and compound interest.
print("  {0}  {1}".format("Simple Interest", "Compound Interest"))
amount = 1000
simple = amount
compound = amount
for i in range(1, 5):
    simple += .05 * amount
    compound = 1.05 * compound
    print("{0} ${1:,.2f}        ${2:,.2f}".format(i, simple, compound))
      
