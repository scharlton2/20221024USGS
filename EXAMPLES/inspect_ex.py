import inspect
import geometry
from carddeck import CardDeck

deck = CardDeck("Leonard")

things = (
    geometry,  # module
    geometry.circle_area,   # function
    CardDeck,  # class
    CardDeck.get_ranks,  # class method
    deck,   # instance
    deck.shuffle,  # instance method
)

print("Name           Module?  Function?  Class?  Method?")
for thing in things:
    try:
        thing_name = thing.__name__
    except AttributeError:
        thing_name = type(thing).__name__ + " instance"
#        thing_name = "(None)"
    print("{:12s}   {!s:6s}   {!s:6s}     {!s:6s}  {!s:6s}".format(
        thing_name,
        inspect.ismodule(thing),  # test for module
        inspect.isfunction(thing),  # test for function
        inspect.isclass(thing),  # test for class
        inspect.ismethod(thing),
    ))

print()
def spam(p1: int, p2='a', *p3, p4: str, p5: str='b', **p6):  # define a function
    print(p1, p2, p3, p4, p5, p6)

# get argument specifications for a function
print("Function spec for Ham:", inspect.getfullargspec(spam))
print()

# get frame (function call stack) info
print("Current frame:", inspect.getframeinfo(inspect.currentframe()))

from typing import Union
Number = Union[int, float]
def double(x: Number):
    return 2 * x

print(double(5))
print(double(4.8))
print(double('mint'))

