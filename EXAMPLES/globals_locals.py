from pprint import pprint  # import prettyprint function

spam = 42  # global variable
ham = 'Smithfield'


def eggs(fruit):  # function parameters are local
    name = 'Lancelot'  # local variable
    idiom = 'swashbuckling'  # local variable
    print("Globals:")
    pprint(globals())  # globals() returns dict of all globals
    print()
    print("Locals:")
    pprint(locals())  # locals() returns dict of all locals


eggs('mango')

g = globals()
print(f"g['spam']: {g['spam']}")
print(f"g['ham']: {g['ham']}")

g['color'] = 'blue'
print(f"color: {color}")

class Dog:
    def bark(self):
        print("woof woof")

    def sniff(self):
        print("sniff sniff snuff")

d = Dog()
print(f"dir(d): {dir(d)}")

foo = [1, 2, 3]
print(f"dir(foo): {dir(foo)}")




