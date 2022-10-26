#

strings = ['wombat', 'koala', 'kookaburra', 'blue-ringed octopus']

result = [s.upper() for s in strings]  # Using a list comprehension, which is usually simpler than map()
print(result)

result = map(str.upper, strings)  # Using map to copy list to upper case
print(result)
print(list(result))

# result = list(map(len, strings))  # Using map to get list of string lengths
# print(result)

words = "   sys   ", "   boom   ",    "bah"
lengths = map(len, map(str.strip, words))
print(list(lengths))

lengths = [len(w.strip()) for w in words]
print(lengths)




