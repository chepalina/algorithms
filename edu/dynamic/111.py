# Без трех единиц
# Определите количество последовательностей из нулей и единиц длины N (длина - это общее количество нулей и едииниц), в которых никакие три единицы не стоят рядом.
#
# Вводится натуральное число N, не превосходящее 40.
#
# Выходные данные
# Выведите количество искомых последовательностей. Гарантируется, что ответ не превосходит 231 − 1.

# 1 0 <- 2
# 11 00 10 01 <- 4
# ~111~ 000 110 101 011 001 010 100


def thee_ones(n: int):

    first = 2
    second = 4
    third = 7

    res = 0

    for _ in range(4, n + 1):
        res = first + second + third
        first, second, third = second, third, res

    return res
    # third = dp[i-1] + dp[i-2] + dp[i-3]
