
names = open('p022_names.txt', 'r').read().replace('"', '').split(',')
names.sort()

def get_value(name):
    total = 0
    for c in name:
        total += ord(c) - ord('A') + 1
    return total

total = 0
for i in range(len(names)):
    name = names[i]
    total += get_value(name) * (i + 1)

print total
