## Big Cross-Out Swindle
startingWord = "NAISNIENLGELTETWEORRSD"
crossedOutLetters = ""
remainingLetters = ""
oddLetter = True
for ch in startingWord:
    if oddLetter:
        crossedOutLetters += ch
    else:
        remainingLetters += ch
    oddLetter = not oddLetter
print("Starting word:", startingWord)
spreadoutWord = ""
for ch in crossedOutLetters:
    spreadoutWord += ch + " "
crossedOutLetters = spreadoutWord.rstrip()
spreadoutWord = ""
for ch in remainingLetters:
    spreadoutWord += ch + " "
remainingLetters = spreadoutWord.rstrip()            
print("Crossed-out letters:", crossedOutLetters)
print("Remaining letters:", remainingLetters)
