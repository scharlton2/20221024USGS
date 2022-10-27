
# super() search parent classes

class SpamBase:
    def __init__(self, a, b):
        print("Hello from SpamBase.__init__()")

class Ham(SpamBase):
    def __init__(self, a, b, c):
        super().__init__(a, b)

class Cheese(SpamBase):
    pass

print("creating instance of Spam")
s = Spam(1, 2)
print("creating instance of Ham")
h = Ham(1, 2, 3)
print("creating instance of Cheese")
c = Cheese(1, 2)

