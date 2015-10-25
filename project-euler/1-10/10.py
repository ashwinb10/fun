import sys
import math

n = int(sys.argv[1])

primes = [2, 3, 5, 7, 11]
for curr in range(primes[-1] + 2, n, 2):
    is_prime = True
    for prime in primes:
        if prime > math.sqrt(curr):
            break
        if curr % prime == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(curr)
print sum(primes)
