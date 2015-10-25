
def calc_pentagonal(n):
    return n * (3*n-1) / 2

max_pent = 10000 # generate first 10k pentagonal numbers
pentagonals = set()
pentagonals_dict = dict()
for i in range(1, max_pent+1):
    value = calc_pentagonal(i)
    pentagonals.add(value)
    pentagonals_dict[i] = value

def find_min_diff():
    i = 2
    while True:
        pent_i = pentagonals_dict[i]
        for j in range(i - 1, 0, -1):
            pent_j = pentagonals_dict[j]
            if (pent_i + pent_j) in pentagonals and (pent_i - pent_j) in pentagonals:
                return pent_i - pent_j
        i += 1

print find_min_diff()
