import math

def is_prime(n):
    for prime in primes_list:
        if n % prime == 0:
            return False
    return True

primes = set([2, 3, 5, 7, 11])
primes_list = [2,3,5,7,11]

def get_prime_factors(n):
    factors = set() 
    for prime in primes_list:
        if n <= 1:
            break
        while n % prime == 0:
            factors.add(prime)
            n /= prime
    return factors


curr = 12
curr_consec = 0

while True:
    if is_prime(curr):
        primes_list.append(curr)
        factors = set([curr])
    else:
        factors = get_prime_factors(curr)

    if len(factors) == 4:
        curr_consec += 1
        if curr_consec == 4:
            print curr - 3
            break
    else:
        curr_consec = 0
    curr += 1
    
    
