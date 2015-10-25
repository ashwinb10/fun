words = open('p042_words.txt', 'r').read().replace('"', '').split(',')

word_values = []
for word in words:
    value = 0
    for c in word:
        value += ord(c) - ord('A') + 1
    word_values.append(value)

triangle_numbers = set()
max_value = max(word_values)
index = 0
while True:
    index += 1
    num = index * (index + 1) / 2
    triangle_numbers.add(num)
    if num >= max_value:
        break

total = 0
for value in word_values:
    if value in triangle_numbers:
        total += 1

print total
