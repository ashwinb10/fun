
def get_cycle_len(n):
    curr_rem = 1

    remainders = {}
    index = 0
    while True:
        if curr_rem == 0:
            return 0
        remainders[curr_rem] = index

        curr_rem *= 10

        divisor = curr_rem / n
        curr_rem = curr_rem % n

        index += 1

        if curr_rem in remainders:
            return index - remainders[curr_rem]


max_divisor = -1
max_len = 0
for i in range(1,1000):
    cycle_len = get_cycle_len(i)
    if cycle_len > max_len:
        max_len = cycle_len
        max_divisor = i

print max_divisor
