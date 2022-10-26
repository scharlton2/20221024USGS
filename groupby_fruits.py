from itertools import groupby

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

def first_letter(fruit):
    return fruit[0]

sorted_fruits = sorted(fruits, key=first_letter)

for key, value in groupby(sorted_fruits, key=first_letter):
    print(key, list(value))
