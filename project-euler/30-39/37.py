import math

def is_prime(n):
    if n == 2:
        return True
    for i in range(2, int(math.ceil(math.sqrt(n))) + 1):
        if n % i == 0:
            return False
    return True

def get_truncations(n):
    n = str(n)
    truncations = []
    for i in range(len(n) - 1):
        truncations.append(int(n[i + 1:]))
        truncations.append(int(n[:i + 1]))
    return truncations


primes = set([2, 3, 5, 7])
curr = 11
num_truncable = 0
total = 0
while num_truncable < 11:
    if is_prime(curr):
        primes.add(curr)
        is_truncable = True
        for truncation in get_truncations(curr):
            if truncation not in primes:
                is_truncable = False
                break
        if is_truncable:
            print curr
            num_truncable += 1
            total += curr
    curr += 1

print total
