from pprint import pprint
from collections import defaultdict

silly_dict = defaultdict(lambda: 0)

silly_dict['wombat'] = 32
silly_dict['koala'] = 18
silly_dict['wallaby'] = 9
print(f"silly_dict: {silly_dict}")
print(f"silly_dict['wombat']: {silly_dict['wombat']}")

print(f"silly_dict['kangaroo']: {silly_dict['kangaroo']}")
print()




fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

fruits_by_letter = defaultdict(list)
for fruit in fruits:
    letter = fruit[0]
    fruits_by_letter[letter].append(fruit)
pprint(fruits_by_letter)


