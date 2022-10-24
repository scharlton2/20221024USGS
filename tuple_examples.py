

my_list = ['a', 'b', 'c']
my_dict = {'a': 1, 'b': 2, 'c': 3}
my_set = {'a', 'b', 'c'}
my_tuple = 'a', 'b', 'c'
my_other_tuple = ('a', 'b', 'c')
my_list_of_tuples = [('a', 'b', 'c'), ('d', 'e', 'f')]

junk = [1, 2, 3], 5, 9
print(f"type(junk): {type(junk)}")

# h = hash(junk)
# print(f"h: {h}")



"""
struct person {
    char *fname;
    char *lname;
    int age;
}
"""


person = 'Bill', 'Gates', 'Microsoft', '1955-10-28'
print(f"person: {person}")
print(f"person[0]: {person[0]}")

# str list tuple bytes

a, b, c, d = person   # iterable unpacking



people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', 'NeXT', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Grace', 'Hopper', 'COBOL', '1906-12-09'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', 'Git', '1969-12-28'),
]

print(f"people[0]: {people[0]}")
print(f"people[0][0]: {people[0][0]}")
print(f"people[0][0][0]: {people[0][0][0]}")

for first_name, last_name, *products, _ in people:
    print(first_name, last_name, products)

data = [('NC', 'Raleigh'), ('CO', 'Denver'), ('NJ', 'Trenton')]

for state, capital in data:
    print(f"{state}: {capital}")

for x in people:
    first_name, last_name, *products, _ = x
    print(first_name, last_name, products)
print()

fruits = ['apple', 'banana', 'cherry']
for i, fruit in enumerate(fruits):
    print(i, fruit)
print()
print(f"list(enumerate(fruits)): {list(enumerate(fruits))}")


def add(x, y):
    return x + y

print(f"add(5, 3): {add(5, 3)}")
x = 10
y = 22
print(f"add(x, y): {add(x, y)}")
values = [18, 91]
print(f"add(values[0], values[1]): {add(values[0], values[1])}")
print(f"add(*values): {add(*values)}")


values = ['a', 'b', 'c', 'd', 'e', 'f']
x, y, *z = values
print(x, y, z)
x, *y, z = values
print(x, y, z)
*x, y, z = values
print(x, y, z)






