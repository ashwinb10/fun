import math
import itertools

def is_prime(n):
    if n == 2:
        return True
    for i in range(2, int(math.ceil(math.sqrt(n))) + 1):
        if n % i == 0:
            return False
    return True

# sum(1-9) = 45; sum(1-8) = 36 --> since they're divisible by 3, they're composite
# try all 7-digit pandigitals

permutations = itertools.permutations('1234567')
max_prime = 0
for permutation in permutations:
    num = int(''.join(permutation))
    if num > max_prime and is_prime(num):
        max_prime = num

print max_prime

