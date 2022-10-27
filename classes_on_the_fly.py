
class Animal:
    pass


class Dog(Animal):
    def bark(self):
        print("woof! woof!")


def bark(self):
    print("woof! woof!")

Dog = type('Dog', (Animal,), {'bark': bark})

d = Dog()
d.bark()
print(type(d))
print(isinstance(d, Dog))
print(isinstance(d, Animal))
print(issubclass(Dog, Animal))


