# E. Электрички и статистика
# https://codeforces.com/problemset/problem/675/E?locale=ru

"""Вася каждый день ездит на электричке. В Васином городе есть n остановок, причём на i-й остановке можно купить билет до любой остановки от (i + 1)-й до ai-й. На конечной остановке билеты не продаются.

Пусть ρi, j — минимальное количество билетов, которое нужно купить, чтобы добраться от i-й остановки до j-й. Вася любит собирать всякую бесполезную статистику, поэтому он просит вас найти сумму всех значений ρi, j по всем 1 ≤ i < j ≤ n.

Входные данные
В первой строке входных данных записано единственное целое число n (2 ≤ n ≤ 100 000) — количество остановок.

Во второй строке записано n - 1 целое число ai (i + 1 ≤ ai ≤ n) — означающее, что на остановке i можно купить билет на электричку до любой остановки от i + 1 до ai включительно.

Выходные данные
Выведите сумму ρi, j по всем 1 ≤ i < j ≤ n."""


def stat(array: list) -> int:

    # Сложность O(1)
    stops_count = len(array)
    dp = [[0] * stops_count for _ in array]

    # O(N)
    for i in range(stops_count - 1):
        dp[i][i] = 0
        dp[i][i + 1] = 1

    # O(N*N)
    for i in range(stops_count - 3, -1, -1):
        for j in range(i + 2, stops_count):
            print(i, j)
            if array[i] >= j + 1:
                dp[i][j] = dp[i + 1][j]
            else:
                dp[i][j] = dp[i + 1][j] + 1

    print(dp)

    # O(N*N)
    tickets_sum = 0
    for i in range(0, stops_count):
        for j in range(i + 1, stops_count):
            tickets_sum += dp[i][j]

    return tickets_sum


# O(N) + O(N*N) -> O(N*N)

# print([i for i in range(5-2, -1, -1)])


assert stat([4, 4, 4, 0]) == 6
assert stat([2, 3, 5, 5, 0]) == 17, stat([2, 3, 5, 5, 0])
