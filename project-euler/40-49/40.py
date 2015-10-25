curr_index = 0
total = 1
curr_num = 1
next_index = 1
while curr_index <= 1000000:
    curr_num_str = str(curr_num)
    curr_len = len(curr_num_str)
    if curr_len + curr_index >= next_index:
        total *= int(curr_num_str[next_index - curr_index - 1])
        next_index *= 10
    curr_index += curr_len
    curr_num += 1

print total


