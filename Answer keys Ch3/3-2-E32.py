## Convert a word to Pig Latin.
word = input("Enter word to translate: ")
word = word.lower()
firstLetter = word[0]
if firstLetter in "aeiou":
    word += "way"
else:
    listOfVowelPositions = []
    if 'a' in word:
        listOfVowelPositions.append(word.find('a'))
    if 'e' in word:
        listOfVowelPositions.append(word.find('e'))
    if 'i' in word:
        listOfVowelPositions.append(word.find('i'))       
    if 'o' in word:
        listOfVowelPositions.append(word.find('o'))
    if 'u' in word:
        listOfVowelPositions.append(word.find('u'))   
    positionOfFirstVowel = min(listOfVowelPositions)
    word = word[positionOfFirstVowel:] + word[:positionOfFirstVowel] + "ay"
print("The word in Pig Latin is " + word + ".")
