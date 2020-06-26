## Determine if a word or phrase is a palindrome.
phrase = input("Enter a word or phrase: ")
phrase = phrase.upper()
strippedPhrase = ""
for char in phrase:
    if (48 <= ord(char) <= 57) or (65 <= ord(char) <= 90):
        strippedPhrase += char
flag = True
n = len(strippedPhrase)
for j in range(int(n / 2)):    
    if strippedPhrase[j] != strippedPhrase[n - j - 1]:
        flag = False
        break
if flag:
    print(phrase, "is a palindrome.")
else:
   print(phrase, "is not a palindrome.")

