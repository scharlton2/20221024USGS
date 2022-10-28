
class Dog:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):  # getter property
        return self._name

    @name.setter
    def name(self, name):  # setter property
        if isinstance(name, str):
            self._name = name
        else:
            raise TypeError("Name must be a string")

    # name = property(get_name, set_name, del_name, "doc string")

d1 = Dog("Nelly")
d2 = Dog("Andy")

print(d1.name) # not d1.get_name() or even d1.name()
print(d2.name)

d1.name = "Barbara"
print(d1.name)