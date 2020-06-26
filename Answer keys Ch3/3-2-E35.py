## Validate input.
letter = input("Enter a single uppercase letter: ")
if (len(letter) != 1) or (letter != letter.upper()):
    print("You did not comply with the request.")
