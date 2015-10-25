
# classic dynamic programming solution:

coins = [1, 2, 5, 10, 20, 50, 100, 200]

cache = [0]*201
cache[0] = 1
for coin in coins:
    for i in range(coin, 201):
        cache[i] += cache[i - coin]

print cache[200]
