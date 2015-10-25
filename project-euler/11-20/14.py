
values = dict()

def compute(n):
    if n == 1:
        return 1

    if values.get(n):
        return values[n]

    if n % 2 == 0:
        value = compute(n/2)
    else:
        value = compute(3*n+1)

    value += 1
    values[n] = value
    return value

max_len = 0
max_start = 0
for i in range(1, 1000000):
    l = compute(i)
    if l > max_len:
        max_len = l
        max_start = i

print max_start
