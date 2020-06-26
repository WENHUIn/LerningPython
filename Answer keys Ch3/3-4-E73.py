## Count the number of different vowels in a word.
word = input("Enter a word: ")
word = word.upper()
vowels = "AEIOU"
vowelsFound = []
numVowels = 0
for letter in word:
    if (letter in vowels) and (letter not in vowelsFound):
        numVowels += 1
        vowelsFound.append(letter)
print("Number of vowels:", numVowels)
