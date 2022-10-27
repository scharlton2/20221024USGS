
with open('DATA/mary.txt') as mary_in:  # mary_in.__iter__() -- returns iterator
    print(f"type(mary_in): {type(mary_in)}")
    #  __next__  __iter__
    first_line = next(mary_in)  #   call mary_in.__next__()
    print(f"first_line: {first_line.rstrip()}")
    for line in mary_in:  # next(), next(), next()
        print(f"line.rstrip(): {line.rstrip()}")

