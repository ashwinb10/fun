import math
import sys

i = 0
curr_sum = 0
while True:
    i += 1
    curr_sum += i

    num_divisors = 0
    for divisor in range(1, int(math.sqrt(curr_sum))):
        if curr_sum % divisor == 0:
            num_divisors += 1
    num_divisors *= 2
    if num_divisors > 500:
        print curr_sum
        sys.exit(0)

