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

abundant = set()
abundant_list = list()
for i in range(1, 28124):
    if get_sum_divisors(i) > i:
        abundant.add(i)
        abundant_list.append(i)

total = 0
for i in range(1, 28124):
    is_possible = False
    for j in abundant_list:
        if j >= i:
            break
        if i - j in abundant:
            is_possible = True
            break
    if not is_possible:
        total += i

print total
