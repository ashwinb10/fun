# 9 * (1,2,3,4,5) --> 918273645 
#    --> the solution is either this or must start with 9
# 2-digit numbers:
#   (90-99)*(1,2,3) --> 8-digit number
#   (90-99)*(1,2,3,4) --> 11-digit number
#   --> can't use 2-digit number
# 3-digit numbers:
#   (900-999)*(1,2) --> 7-digit number
#   (900-999)*(1,2,3) --> 11-digit number
#   --> can't use 3-digit number
# --> must be 4-digit number between 9000-9999*(1,2)

# NOTE: can make more efficient by going from 9999 to 9000 and stopping at first solution
max_num = 918273645 # start wtih 9*(1,2,3,4,5)
for i in range(9000, 10000):
    possible_pandigital_str = str(i) + str(i*2)
    possible_pandigital = int(possible_pandigital_str)
    if possible_pandigital < max_num:
        continue

    digits = set()
    for digit in possible_pandigital_str:
        if digit != '0':
            digits.add(digit)
    if len(digits) == 9:
        max_num = possible_pandigital

print max_num
