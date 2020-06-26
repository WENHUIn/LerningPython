## Word replacement.
sentence = input("Enter a sentence: ")
word1 = input("Enter word to replace: ")
word2 = input("Enter replacement word: ")
location = sentence.find(word1)
newSentence = sentence[:location] + word2 + sentence[location + len(word1):]
print(newSentence)



      
             
