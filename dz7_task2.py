# Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.

import random

def merge_sort(array):
    if len(array) < 2:
        return array
    result = []
    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    while len(left) > 0 and len(right) > 0:
        if left[0] > right[0]:
            result.append(right.pop(0))
        else:
            result.append(left.pop(0))
    result += left
    result += right
    return result


MIN_NUM = 0
MAX_NUM = 50 - random.random()
NUM_ELEMENTS = 25

array = [random.uniform(MIN_NUM, MAX_NUM) for _ in range(NUM_ELEMENTS)]

print(f"Исходный массив:", )
for _ in array:
    print(f"{_:.4}, ", end="")
print()

result = merge_sort(array)

print(f"Отсортированный массив:", )
for _ in result:
    print(f"{_:.4}, ", end="")
print()
