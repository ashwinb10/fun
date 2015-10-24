
import math

total = 0
for digit in str(math.factorial(100)):
    total += int(digit)

print total
