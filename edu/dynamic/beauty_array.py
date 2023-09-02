# Вам дан массив 𝑎
# состоящий из 𝑛
# целых чисел. Красота массива – это максимальная сумма какого-то последовательного подотрезка этого массива (этот подотрезок может быть пустым). Например красота массива [10, -5, 10, -4, 1] равна 15, а красота массива [-3, -5, -1] равна 0.
#
# Вы можете выбрать не более одного последовательного подотрезка массива 𝑎
# и домножить все элементы этого подотрезка на 𝑥
# . Вы хотите максимизировать красоту массива после применения такой операции.
#
# Входные данные
# Первая строка содержит два целых числа 𝑛
# и 𝑥
# (1≤𝑛≤3⋅105,−100≤𝑥≤100
#  ) — длина массива 𝑎
# и число 𝑥
# соответственно.
#
# Вторая строка содержит 𝑛
# целых чисел 𝑎1,𝑎2,…,𝑎𝑛
# (−109≤𝑎𝑖≤109
#  ) — сам массив 𝑎
# .
#
# Выходные данные
# Выведите одно число — максимальную красоту массива 𝑎
# после не более одного домножения непрерывного подотрезка этого массива на 𝑥


# -1 -2 4 -3 -6 1

#   -3 8 -2 1 -6
# -2

# dp[0] = 0 8 6 7 1
# dp[1] = 6-10 12 10 22
# dp[2] = -3 14 12 13 7

a = [-3, 8, -2, 1, -6]
x = -2
n = len(a)
dp = [[0 for _ in range(n + 1)] for _ in range(3)]
ans = 0

dp[0][0] = max(0, a[0])
dp[1][0] = dp[0][0] + a[0] * x
dp[2][0] = max(dp[0][0], dp[1][0]) + a[0]

for i in range(1, n):
    dp[0][i] = max(0, dp[0][i - 1]) + a[i]
    dp[1][i] = max(dp[0][i - 1], dp[1][i - 1]) + a[i] * x
    dp[2][i] = max(dp[0][i - 1], dp[1][i - 1], dp[2][i - 1]) + a[i]

    ans = max(ans, dp[0][i], dp[1][i], dp[2][i])

print(ans)
