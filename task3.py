
# Задание 3
# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
#

import random

MIN_LIMIT = 1
MAX_LIMIT = 100
SIZE = 10

array = [random.randint(MIN_LIMIT, MAX_LIMIT) for _ in range(SIZE)]
print(array)

min_item = array[0]
min_index = 0
max_item = array[0]
max_index = 0

for item in enumerate(array):
    if item[1] > max_item:
        max_index, max_item = item
    if item[1] < min_item:
        min_index, min_item = item

array[min_index], array[max_index] = array[max_index], array[min_index]

print(array)
