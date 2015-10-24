prev = 1
curr = 1
index = 2
while True:
    index += 1
    nextNum = prev + curr
    if len(str(nextNum)) >= 1000:
        print index
        break
    prev = curr
    curr = nextNum

