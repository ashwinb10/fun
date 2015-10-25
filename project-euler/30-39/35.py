import math

def is_prime(n):
    if n == 2:
        return True
    for i in range(2, int(math.ceil(math.sqrt(n))) + 1):
        if n % i == 0:
            return False
    return True

primes = set()
for i in range(2, 1000000):
    if is_prime(i):
        primes.add(i)

total = 0
for i in range(2, 1000000):
    is_circular = True
    i_str = str(i)
    for j in range(len(i_str)):
        new_i = int(i_str[j:] + i_str[:j])
        if not new_i in primes:
            is_circular = False
            break
    if is_circular:
        total += 1

print total

