
# 1001 x 1001 square
# number of squares = 501
#   index squares from 0 to 500 --> size of each square = 2n+1 x 2n+1
# top right corner of each square = (2n+1)^2
#   sum of corners = (2n+1)^2 - 12(n)
# define f(n) = {
#   (2n+1)^2 - 12(n), n > 0
#   1,                n = 0

def f(n):
    if n == 0:
        return 1
    return 4*(2*n+1)**2 - 12*n

total = 0
for i in range(0, 501):
    total += f(i)

print total
