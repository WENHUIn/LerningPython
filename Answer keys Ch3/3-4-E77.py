## Display sentence with Boston accent.
sentence = input("Enter a sentence: ")
newSentence = ""
for ch in sentence:
    if ch.upper() != 'R':
         newSentence += ch
print(newSentence)
