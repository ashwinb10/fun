lower = 1
higher = 1
total = 0
while True:
    nextNum = lower + higher
    if nextNum > 4000000:
        break
    if nextNum % 2 == 0:
        total += nextNum
    lower = higher
    higher = nextNum
print total
