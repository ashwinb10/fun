import math

def is_prime(n):
    for prime in primes_list:
        if prime > math.sqrt(n):
            break
        if n % prime == 0:
            return False
    return True

primes_list = [2, 3, 5, 7, 11, 13]
curr = 15
while curr < 1000000:
    if is_prime(curr):
        primes_list.append(curr)
    curr += 2

cache = []
cum_total = 0
for prime in primes_list:
    cum_total += prime
    cache.append(cum_total)

primes_set = set(primes_list)

max_prime = 0
max_consec = 0
for i in range(len(primes_list)):
    for j in range(i - 1 - max_consec, -1, -1):
        diff = cache[i] - cache[j]
        if diff > 1000000:
            break
        if diff in primes_set:
            max_consec = i - j
            max_prime = diff

print max_prime
