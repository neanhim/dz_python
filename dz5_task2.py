#Написать программу сложения и умножения двух шестнадцатеричных чисел.
#При этом каждое число представляется как массив, элементы которого это цифры числа.
#Например, пользователь ввёл A2 и C4F.
#Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
#Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import deque

a = deque(str(input('введите 1 число\n')).upper())
b = deque(str(input('введите 2 число\n')).upper())

to_dec = {str(i): i for i in range(10)}
to_dec.update({'A': 10, "B":  11, "C":  12, "D":  13, "E":  14, "F": 15})
to_hex = {i: str(i) for i in range(10)}
to_hex.update({10: 'A', 11: "B", 12: "C", 13: "D", 14: "F", 15: "F"})

result_sum = deque()


# Делаем одинаковое количество разрядов в обоих числах
while len(a) != len(b):
    if len(a) < len(b):
        a.appendleft("0")
    if len(b) < len(a):
        b.appendleft("0")

# перенос на следующий разряд
in_mind = 0

result_mult = ['0'] * (2 * len(a))

for i in range(1, len(a) + 1):
    result_sum.appendleft(to_hex[(to_dec[a[-i]] + to_dec[b[-i]] + in_mind) % 16])
    in_mind =  (to_dec[a[-i]] + to_dec[b[-i]] + in_mind) // 16

# temp_res = [deque() for _ in range(len(b))]
# in_mind = 0
# for i in range(1, len(b) + 1):
# #     for k in range(1, len(a) + 1):
# #                 temp_res[b - 1].appendleft((to_dec[a[-k]] * to_dec[b[-i]] + in_mind) % 16)
# #             elif _ > i - 1:
# #                 temp_res[_].appendleft('0')
# #             in_mind = (to_dec[a[-k]] * to_dec[b[-i]] + in_mind) // 16
# #
# #         temp_res[k].appendleft()
# не успел закончить

print("Сумма чисел равна ", *list(result_sum), sep="")
