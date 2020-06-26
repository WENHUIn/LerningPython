## Marketing terms.
purchasePrice = float(input("Enter purchase price: "))
sellingPrice = float(input("Enter selling price: "))
markup = sellingPrice - purchasePrice
percentageMarkup = 100 * (markup / purchasePrice)
profitMargin = 100 * (markup / sellingPrice)
print("Markup:", '$' + str(round(markup, 2)))
print("Percentage markup:", str(round(percentageMarkup, 2)) + '%')
print("Profit margin:", str(round(profitMargin, 2)) + '%')
