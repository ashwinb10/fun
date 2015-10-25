# using 2540160 as upper limit because the value for 9,999,999 would be 7*(9!)=2,540,160

import math

cache = {}
for i in range(10):
    cache[i] = math.factorial(i)

total = 0
for i in range(3, 2540160):
    fact_sum = 0
    for digit in str(i):
        digit = int(digit)
        fact_sum += cache[digit]
    if fact_sum == i:
        total += i

print total

