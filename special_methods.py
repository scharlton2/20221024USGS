
class Dog:
    def __len__(self):
        return 19

    def __add__(self, other):
        return "puppies"

    def __getitem__(self, index):
        return "wombats!"

d = Dog()
print(f"len(d): {len(d)}")
# len(d)   <==>  Dog.__len__(d)

d2 = Dog()

print(d + d2)

print(d[4])

