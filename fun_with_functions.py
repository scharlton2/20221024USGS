import operator as op

def spam(callable):
    print(f"func: {callable}")
    result = callable()
    print(f"result: {result}")

def ham():
    return 42

spam(ham)

def toast():
    return "Um, toasty"

spam(toast)

class Dog:
    def bark(self):
        print("woof woof")

spam(Dog)


def foo(name):
    def bar():
        return name.upper()
    
    return bar

x = foo('mary')
print(f"x: {x}")
result = x()
print(f"result: {result}")

spam(lambda: 100)

nums = [800, 80, 1000, 32, 255, 400, 5, 5000]

n = sorted(nums, key=lambda i: str(i))
print(f"n: {n}")

print(5 + 10)
print(op.add(5, 10))

def my_func(adder, x, y):
    return adder(x, y)

def do_addition(a, b):
    return a + b

print(my_func(do_addition, 10, 12))
print(my_func(lambda m, n: m + n, 18, 19))
print(my_func(op.add, 100, 98))

print(dir(op))








