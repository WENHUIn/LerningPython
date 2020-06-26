## Count the number of vowels in a phrase.
total = 0
phrase = input("Enter a phrase: ")
phrase = phrase.lower()
for ch in phrase:
    if ch in "aeiou":
        total += 1
print("The phrase contains", total, "vowels.")

