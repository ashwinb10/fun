import math

def get_sum_divisors(n):
    total = 0
    for i in range(1, int(math.ceil(math.sqrt(n) + 0.00001))):
        if n != i and n % i == 0:
            j = n / i
            total += i
            if n != j and i != j:
                total += j
    return total

if __name__ == '__main__':
    cache = {}
    for i in range(1, 10000):
        cache[i] = get_sum_divisors(i)

    amicable_sum = 0
    for i in range(1, 10000):
        if i != cache[i] and i == cache.get(cache[i], -1):
            amicable_sum += i

    print amicable_sum
