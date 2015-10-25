import sys
if len(sys.argv) == 1:
    print 'Please enter a number'
    sys.exit(1)
n = int(sys.argv[1])

def gcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    r = a % b
    return gcd(b, r)

def lcm(a, b):
    return a * b / gcd(a, b)

total = 1
for i in range(1, n+1):
    total = lcm(total, i)

print total
