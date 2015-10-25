from collections import Counter

def is_prime(n):
    for prime in primes:
        if n % prime == 0:
            return False
    return True

primes = [2, 3, 5, 7, 11]
primes_over = []
curr = 13
while curr < 10000:
    if is_prime(curr):
        primes.append(curr)
        if len(str(curr)) == 4:
            primes_over.append(curr)
    curr += 2

primes_over_set = set(primes_over)

def find_answer():
    for i in range(len(primes_over)):
        prime1 = primes_over[i]
        if prime1 == 1487:
            continue
        for j in range(i + 1, len(primes_over)):
            prime2 = primes_over[j]
            prime3 = prime2 + (prime2 - prime1)
            if prime3 in primes_over:
                prime1_c = Counter(str(prime1))
                prime2_c = Counter(str(prime2))
                prime3_c = Counter(str(prime3))
                if prime1_c == prime2_c and prime2_c == prime3_c:
                    return str(prime1) + str(prime2) + str(prime3)

print find_answer()

