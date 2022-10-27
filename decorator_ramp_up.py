from functools import wraps

def alpha(func):

    @wraps(func)
    def _(*args, **kwargs):
        print("Hi Mom!")
        result = func(*args, **kwargs)
        return result.upper() * 2
    return _

@alpha
def beta():
    print("Hello from beta()")
    return 'bbbb'

# beta = alpha(beta)

print(beta)
print(beta())

@alpha
def delta():
    print("Hello from delta()")
    return 'dddd'

# delta = alpha(delta)
print(delta())

@alpha
def epsilon(x, y):
    print("hello from epsilon()")
    print(x, y)
    return 'eeee'

print(epsilon(1, 2))

for f in beta, epsilon, delta:
    print(f.__name__)

# @foo
# def bar():
#    pass

#  bar = foo(bar)


# @spam(a, b, c)
# def ham():
#    pass


#  ham = spam(a, b, c)(ham)
















