import sys
n = int(sys.argv[1])

primes = [2, 3, 5, 7, 11, 13]
while len(primes) < n:
    curr = primes[-1] + 1
    while True:
        is_prime = True
        for prime in primes:
            if curr % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(curr)
            break
        else:
            curr += 1

print primes[-1]
