import itertools

primes = [2, 3, 5, 7, 11, 13, 17]

total = 0
for permutation in itertools.permutations('0123456789'):
    if permutation[0] == '0':
        continue
    num_str = ''.join(permutation)
    num = int(num_str)

    is_all_divisible = True
    for i in range(len(primes)):
        n = int(num_str[i+1:i+4])
        if n % primes[i] != 0:
            is_all_divisible = False
            break
    
    if is_all_divisible:
        total += num

print total

