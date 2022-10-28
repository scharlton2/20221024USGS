from president import President

colors = ['red', 'purple', 'ecru', 'ochre']

for attr in dir(colors):
    value = getattr(colors, attr)
    print(attr, type(value), end=" ")
    if isinstance(value, (int, float, str)):
        print(value)
    else:
        print()


p = President(26)
print(p)
print(p.first_name, p.last_name)
field = "party"
print(getattr(p, field))
print(getattr(p, "birth_place"))

print(hasattr(p, 'nickname'))

# setattr(p, "first_name", "Stanley")
# print(getattr(p, "first_name"))

class Dog:
    pass


def bark(self):
    print("woof woof")

setattr(Dog, 'bark', bark)

d = Dog()
d.bark()




