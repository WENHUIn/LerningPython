## Remove dashes from a phone number.
phoneNum = input("Enter a telephone number: ")
numWithoutDashes = ""
for ch in phoneNum:
    if ch != '-':
        numWithoutDashes += ch
print("Number without dashes is", numWithoutDashes + '.')   
