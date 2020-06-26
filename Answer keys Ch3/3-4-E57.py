## Determine if the letters of a word are in alphabetical order.
word = input("Enter a word: ")
firstLetter = ""
secondLetter = ""
flag = True
for i in range(0, len(word) - 1):
    firstLetter = word[i]
    secondLetter = word[i + 1]
    if firstLetter > secondLetter:
        flag = False
        break
if flag:
    print("Letters are in alphabetical order.")
else:    
    print("Letters are not in alphabetical order.")
