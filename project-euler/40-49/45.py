# note: all hexagonal numbers are triangular
import math

def is_pentagonal(n):
    val = (math.sqrt(24*n + 1)+1) / 6.0
    return val == int(val)

i = 286
while True:
    n = i*(2*i-1)
    if is_pentagonal(n):
        print n
        break
    i += 1

        
