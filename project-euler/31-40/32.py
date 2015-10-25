import itertools

total = 0

permutations = itertools.permutations('123456789')
products = set()
for permutation in permutations:
    product = int(''.join(permutation[5:]))
    for i in range(1, 5):
        multiplicand = int(''.join(permutation[:i]))
        multiplier = int(''.join(permutation[i:5]))
        if multiplier * multiplicand == product:
            products.add(product)
            break

print sum(products)
