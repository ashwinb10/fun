
fifth_powers = {}
for i in range(10):
    fifth_powers[str(i)] = i**5

# 9**5 * 6 < 999999
#   thus, all numbers > 999999 cannot be written as sum of 5th powers of their digits
total = 0
for i in range(2, 9**5 * 6):
    digit_sum = 0
    for digit in str(i):
        digit_sum += fifth_powers[digit]
    if digit_sum == i:
        total += i

print total

