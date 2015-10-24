
digits = {
    1: 3,
    2: 3,
    3: 5,
    4: 4,
    5: 4,
    6: 3,
    7: 5,
    8: 5,
    9: 4,
    0: 4
}
teens = {
    10: len('ten'),
    11: len('eleven'),
    12: len('twelve'),
    13: len('thirteen'),
    14: len('fourteen'),
    15: len('fifteen'),
    16: len('sixteen'),
    17: len('seventeen'),
    18: len('eighteen'),
    19: len('nineteen')
}
tens_digits = {
    2: len('twenty'),
    3: len('thirty'),
    4: len('forty'),
    5: len('fifty'),
    6: len('sixty'),
    7: len('seventy'),
    8: len('eighty'),
    9: len('ninety')
}
ones_digits = {
    1: 3,
    2: 3,
    3: 5,
    4: 4,
    5: 4,
    6: 3,
    7: 5,
    8: 5,
    9: 4,
    0: 0
}

def get_count(num):
    if num == 1000:
        return len('one') + len('thousand')

    count = 0

    # for 100's place
    if num / 100 > 0:
        count += len('hundred') + digits[num/100]
        if num % 100 > 0:
            count += len('and')
        else:
            return count

    # for last 2 digits
    num = num % 100
    tens = num / 10
    if tens == 0:
        count += digits[num]
    elif tens == 1:
        count += teens[num]
    else:
        count += tens_digits[num/10] + ones_digits[num % 10]

    return count

total = 0
for i in range(1, 1001):
    total += get_count(i)
print total
