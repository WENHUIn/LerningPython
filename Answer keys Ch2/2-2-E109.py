## Analyze a number.
number = input("Enter number: ")   # Note: number is a string
decimalPoint = number.find('.')
print(decimalPoint, "digits to left of decimal point")
print(len(number) - decimalPoint - 1, "digits to right of decimal point")


      
             
