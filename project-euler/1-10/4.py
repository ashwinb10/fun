
def is_palindrome(n):
    n = str(n)
    for i in range(len(n)/2):
        if n[i] != n[len(n) - i - 1]:
            return False
    return True

products = list()
for i in range(900,1000):
    for j in range(900, 1000):
        product = i * j
        if is_palindrome(product):
            products.append(product)
print max(products)
