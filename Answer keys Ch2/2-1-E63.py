price = 19.95
discountPercent = 30
markdown = (discountPercent / 100) * price
price = price - markdown
print(round(price, 2))
