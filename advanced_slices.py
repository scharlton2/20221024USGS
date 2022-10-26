
fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

print(f"fruits[0]: {fruits[0]}")
print(f"fruits[-1]: {fruits[-1]}")
print(f"fruits[:4]: {fruits[:4]}")
print(f"fruits[-5:]: {fruits[-5:]}")
print(f"fruits[4:9]: {fruits[4:9]}")
print()
print(f"fruits[2:9:2]: {fruits[2:9:2]}")
print(f"fruits[2:9:3]: {fruits[2:9:3]}")

print(f"fruits: {fruits}")
fruits[0] = "boysenberry"
print(f"fruits: {fruits}")

new_fruits = ['gooseberry', 'raspberry', 'durian']

fruits[1:3] = new_fruits
print(f"fruits: {fruits}")



