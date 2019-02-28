
# Задание 4
# Определить, какое число в массиве встречается чаще всего.
#

import random

MIN_LIMIT = 0
MAX_LIMIT = 3
SIZE = 10

array = [random.randint(MIN_LIMIT, MAX_LIMIT) for _ in range(SIZE)]
print(array)

item_freq = {}

for item in array:
    if item in item_freq:
        item_freq[item] += 1
    else:
        item_freq[item] = 1

most_frequent_item = 0
max_freq = 0
for item in item_freq:
    if item_freq[item] > max_freq:
        max_freq, most_frequent_item = item_freq[item], item

print(f"Число {most_frequent_item} встречается чаще всего, а именно {max_freq} раз(а)")
