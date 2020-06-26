## Determine if a word contains every vowel.
word = input("Enter a word: ")
word = word.upper()
vowels = "AEIOU"
isVowelWord = True
for letter in vowels:
    if letter not in word:
        isVowelWord = False
        break
if isVowelWord:
    print(word, "is a vowel word.")
else:
    print(word, "is a not a vowel word.")
