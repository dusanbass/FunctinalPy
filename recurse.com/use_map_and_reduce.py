# Map -	takes a function and a collection of items.
#	Makes new collection, runs the function on item

name_lengths = map(len, ["Mary", "Isla", "Samwise"])
print name_lengths

# Square every number
squares = map(lambda x: x * x, [0, 1, 2, 3, 4])
print squares

import random
names = ['Mary', 'Pipin', 'Sam']
secret_names = map(lambda x: random.choice(['Mr. Pink', 'Mr. Orange', 'Mr. Blonde']), names)
print secret_names

# Exercise 1.
hash_names = map(lambda x: hash(x), names)
print hash_names
# sol
hash_names_sol = map(hash, names)
print hash_names_sol

# Reduce
#	takes function and a collection of items.
#	Returns a value that is created by combining them
sum = reduce(lambda a, x: a + x, [0, 1, 2, 3, 4])
print sum
# x is the current item being iterated over.
# a is the accumulator
