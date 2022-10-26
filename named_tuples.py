from collections import namedtuple
from dataclasses import dataclass, field

person = "Bob", "Smith", "Denver", "CO"

print(person[0], person[-1])

Person = namedtuple('Person', "first_name last_name city state")

p = Person("Bob", "Smith", "Denver", "CO")

print(f"p: {p}")
print(f"p.first_name: {p.first_name}")
print(p.first_name, p.last_name)
print(p[0], p[1])

@dataclass
class Human:
    first_name: str  = field(init=False)
    last_name: str
    city: str
    state: str



h = Human("Grosvenor", "Topeka", "KS")
print(h)
print(h.last_name, h.first_name)

h.last_name = 'Scrooge'
print(h)






