import fractions

def check(a, b, c, d):
    if float(a) / b == float(c) / d:
        return True

def is_curious(num, den):
    num_str = str(num)
    den_str = str(den)

    for i in range(2):
        for j in range(2):
            if num_str[i]==den_str[j] and check(num, den, int(num_str[1-i]), int(den_str[1-j])):
                return True
    return False

total_num = 1
total_den = 1
for numerator in range(10, 100):
    if numerator % 10 == 0:
        continue

    for denominator in range(10, 100):
        if denominator % 10 == 0:
            continue

        if numerator / denominator >= 1:
            continue

        if is_curious(numerator, denominator):
            total_num *= numerator
            total_den *= denominator

print total_den / fractions.gcd(total_num, total_den)
        

