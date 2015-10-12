import sys

n = int(sys.argv[1])
squared_sum = (n * (n + 1) / 2) ** 2

sum_squares = 0
for i in range(1, n+1):
    sum_squares += i ** 2

print squared_sum - sum_squares
