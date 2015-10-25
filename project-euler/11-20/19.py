
def num_days(month, year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    
    if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
        return 28
    return 29

curr_day = 1
total = 0
for year in range(1900, 2001):
    for month in range(1, 13):
        if curr_day == 0 and year != 1900:
            total += 1
        curr_day += num_days(month, year)
        curr_day %= 7

print total

