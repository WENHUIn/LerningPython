## Validate a credit card number.
num = input("Enter a credit card number: ")
evenSum = 0
oddSum = 0
for i in range(0, len(num), 2):
    digit = int(num[i]) * 2
    if digit >= 10:
        digit -= 9
    evenSum += digit
for i in range(1, len(num) + 1, 2):
    oddSum += int(num[i])
if (evenSum + oddSum) % 10 == 0 and len(num) == 14:
    print("The number is valid.")
else:
    print("The number is not valid.")
