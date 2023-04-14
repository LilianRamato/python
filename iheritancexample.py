class Animal:
    def __init__(self,name):
        self.myname=name

    def talk(self):
        raise NotImplementedError("Subclass must implement abstract method")
class Cat(Animal):
    def talk(self):
        return "meow"
class Dog(Animal):
    def talk(self):
        return "woof"
class Cow(Animal):
    def talk(self):
        return "moooow"
class Horse(Animal):
    def talk(self):
        return"neigh"
class Donkey(Animal):
    def talk(self):
        return "neighs"

paka=Cat("whiskers")
doggy=Dog("fido")
funryy=Cow("kirry")
lensy=Horse("sparks")
bennly=Donkey("neo")

print(paka.myname + " :" + paka.talk())
print(doggy.myname + " :" + doggy.talk())
print(funryy.myname + " :" + funryy.talk())
print(lensy.myname + " :" + lensy.talk())
print(bennly.myname + " :" + bennly.talk())


