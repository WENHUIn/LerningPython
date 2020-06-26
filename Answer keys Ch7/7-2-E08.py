def main():
    creature = Vertebrate()
    print(creature)
    creature = Arthropod()
    print(creature)

class Animal:
    def __init__(self, feature="I can move."):
        self._feature = feature
        
    def __str__(self):
        return self._feature

class Vertebrate(Animal):
    def __init__(self, feature="I have a backbone."):
        self._feature = feature
        
    def __str__(self):
        return self._feature

class Arthropod(Animal):
    def __init__(self, feature="I have jointed limbs and no backbone."):
        self._feature = feature

    def __str__(self):
        return self._feature   

main()
