
def is_palindrome(n):
    for i in range(len(n)/2):
        if n[i] != n[len(n) - i - 1]:
            return False
    return True

def to_binary(n):
    return bin(n)[2:]

total = 0
for i in range(1, 1000000):
    if is_palindrome(str(i)) and is_palindrome(to_binary(i)):
        total += i

print total
