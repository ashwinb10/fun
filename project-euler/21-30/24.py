import itertools

permutations = list(itertools.permutations('0123456789'))
permutations.sort()
print permutations[999999]
