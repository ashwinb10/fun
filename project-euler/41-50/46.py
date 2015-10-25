import math

def is_square(n):
    sqrt = math.sqrt(n)
    return n % sqrt == 0

def is_prime(n):
    if n == 2:
        return True
    for i in range(2, int(math.ceil(math.sqrt(n))) + 1):
        if n % i == 0:
            return False
    return True

def find_answer():
    primes = set([3, 5, 7, 11, 13])
    curr = 13
    while True:
        curr += 2

        if is_prime(curr):
            primes.add(curr)
            continue

        is_possible = False
        for prime in primes:
            if is_square((curr - prime)/2):
                is_possible = True
                break

        if not is_possible:
            return curr

print find_answer()
