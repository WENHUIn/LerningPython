faceValue = float(input("Enter face value of bond: "))
couponRate = float(input("Enter coupon interest rate: "))
interest = faceValue * couponRate
marketPrice = float(input("Enter current market price: "))
yrsUntilMaturity = float(input("Enter years until maturity: "))
a = (faceValue - marketPrice) / yrsUntilMaturity
b = (faceValue + marketPrice) / 2
ytm = (interest + a) / b
print("Approximate YTM: {0:.2%}".format(ytm))


