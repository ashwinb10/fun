# a^2 + b^2 = c^2
# a + b + c = p
#       c = p - a - b
#       a^2 + b^2 = (p - a - b)^2 = p^2 + a^2 + b^2 - 2ap + 2ab - 2bp
#           2bp - 2ab = p^2 - 2ap
#           b = (p^2-2ap)/(2p-2a)

max_p = 0
max_solutions = 0
for p in range(2, 1001):
    num_solutions = 0
    for a in range(1, p/3):
        if (p**2 - 2*a*p) % (2*p - 2*a) == 0:
            num_solutions += 1
    if num_solutions > max_solutions:
        max_solutions = num_solutions
        max_p = p

print max_p

