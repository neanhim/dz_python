
# Задание 7
# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.
#

import random

MIN_LIMIT = -100
MAX_LIMIT = 100
SIZE = 10

array = [random.randint(MIN_LIMIT, MAX_LIMIT) for _ in range(SIZE)]
print(array)

min_elem_one = MAX_LIMIT
min_elem_two = MAX_LIMIT

for item in array:
    if item <= min_elem_one:
        min_elem_two = min_elem_one
        min_elem_one = item
        continue
    if item < min_elem_two:
        min_elem_two = item

print(f"Наименьший элемент в массиве - {min_elem_one}, следующий за ним - {min_elem_two}")
