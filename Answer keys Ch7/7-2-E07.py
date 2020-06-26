def main():
    individual = Cowboy()
    individual.sayGreeting()
    individual = Aussie()
    individual.sayGreeting()

class Person:
    def __init__(self, salutation="Hello"):
        self._salutation = salutation
        
    def sayGreeting(self):
        print(self._salutation)

class Cowboy(Person):
    def __init__(self, salutation="Howdy"):
        self._salutation = salutation
        
    def sayGreeting(self):
        print(self._salutation)

class Aussie(Person):
    def __init__(self, salutation="G'day mate"):
        self._salutation = salutation

    def sayGreeting(self):
        print(self._salutation)

main()
