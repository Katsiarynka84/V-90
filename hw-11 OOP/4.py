class Animal:
    def reply(self):
        return self.speak()
class Mammal(Animal):
    def speak(self):
        return 'Muuu'
class Cat(Mammal):
    def speak(self):
        return 'miu'
class Dog:
    def speak(self):
        return f'{Dog.__name__} sais "gau-gau"'
class Primate(Mammal):
    def speak(self):
        return 'Hello world!'
class Hacker(Primate):
    pass

spot = Cat()
data = Hacker()
pet = Dog()
print(pet.speak())
print(spot.reply())
print(data.reply())
