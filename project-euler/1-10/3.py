import math

def get_next_prime_factor(n):
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return i

curr = 600851475143
factors = list()
while True:
    nextFactor = get_next_prime_factor(curr)
    if nextFactor:
        factors.append(nextFactor)
        curr /= nextFactor
    else:
        factors.append(curr)
        break
print max(factors)
