## Encode words by sound with the Soundex System.
word = input("Enter a word to code: ")
code = word[0]
lastChar = ""
for ch in word[1:].lower():
    if ch in "bfpv" and lastChar != '1':
        code += '1'
        lastChar = '1'
    elif ch in "cgjkqsxz" and lastChar != '2':
        code += '2'
        lastChar = '2'
    elif ch in "dt" and lastChar != '3':
        code += '3'
        lastChar = '3'
    elif ch == 'l' and lastChar != '4':
        code += '4'
        lastChar = '4'
    elif ch in "mn" and lastChar != '5':
        code += '5'
        lastChar = '5'
    elif ch == 'r' and lastChar != '6':
        code += '6'
        lastChar = '6'
# Make the code 4 characters long.
extraZeros = 4 - len(code)
if extraZeros > 0:
    code += '0' * extraZeros
else:
    code = code[:4]
print("The coded word is {0}.".format(code))
