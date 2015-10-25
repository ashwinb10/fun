import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

def num_consecutive_primes(a, b):
    total = 0
    curr = 0
    while True:
        if is_prime(curr*curr + a*curr + b):
            total += 1
            curr += 1
        else:
            return total

max_a = -1
max_b = -1
max_primes = -1
for a in range(-999, 1000):
    for b in range(-999, 1000):
        num_primes = num_consecutive_primes(a, b)
        if num_primes > max_primes:
            max_primes = num_primes
            max_a = a
            max_b = b

print max_a * max_b
