#
#
# def check_stones(j, s):
#     matches_count = 0
#     for j_item in j:
#         matches_count += s.count(j_item)
#
#     return matches_count
#
# print (check_stones("ss", "ssdd"))
#
#
# s = "ssdd"
# j = "ss"
#
# result = 0
# for ch in s:
#     if ch in j:
#         result += 1
#
# print(result)

import sys


# 1111 -> 4
# 0000 -> 0
#  -> 0
# 11111001 -> 5
# 100111 -> 3


# max_seq = 0
# max_cur_seq = 0
#
# VALUE = 1
#
# count = sys.stdin.readline().strip()
#
#
# for _ in range(int(count)):
#     x = int(sys.stdin.readline().strip())
#     if x == VALUE:
#         max_cur_seq += 1
#         if max_cur_seq > max_seq:
#             max_seq = max_cur_seq
#     else:
#         max_cur_seq = 0
#
# print(max_seq)

#
#
# import sys
#
# count = sys.stdin.readline().strip()
#
# result = 0
# max = 0
# for i in range(int(count)):
#     el = sys.stdin.readline().strip()
#     if el == '1':
#         result += 1
#     else:
#         if max < result:
#             max = result
#         result = 0
#
# print(max if max > result else result)
#
#


# import sys
# n = int(sys.stdin.readline().strip())
#
# #
# def foo(s, l, r, pairs):
#     """
#      Если правая И левая часть равны заданному лимиту, выводим строку (условие выхода)
#
#      Иначе:
#         если левая часть меньше чем необходимо - добавляем открывающую скобку, увеличиваем левую часть
#         если правая часть меньше - добавляем закрывающую скобку, увеличиваем правую часть
#
#     Пример n = 1
#     Стек вызовов:
#         foo('', 0, 0, 1)
#         foo('(', 1, 0, 1)
#         foo('()', 1, 1, 1)
#          -> возврат print ()
#
#     Пример n = 2
#     Стек вызовов:
#         foo('', 0, 0, 2)
#         - foo('(', 1, 0, 2)
#         - foo('()', 1, 1, 2)
#         foo('(', 1, 0, 2)
#         - foo('((', 2, 0, 2)
#         - foo('(()', 2, 1, 2)
#
#     """
#     # длина строки равна pairs*2
#     if l == pairs and r == pairs:
#         print(s)
#     else:
#         if l < pairs:
#             foo(s + '(', l + 1, r, pairs)
#         if r < l:
#             foo(s + ')', l, r + 1, pairs)
#
#
# foo('', 0, 0, n)


# d1 = {"s": 1, "l":2}
# d2 = {"l":2, "s":1}
#
# print(d1==d2)


# №6

import sys

n = int(sys.stdin.readline().strip())

cities = []

for _ in range(n):
    el = sys.stdin.readline().strip()
    cities.append(tuple(int(e) for e in el.split(" ")))


max_distance = int(sys.stdin.readline().strip())

destination = sys.stdin.readline().strip().split(" ")

city_start = cities[int(destination[0]) - 1]
city_finish = cities[int(destination[1]) - 1]


# print(cities, city_start, city_finish, distance)

all_cities = []


def find_city(city_start, city_finish, cities, iter):

    if iter > 0:
        if not cities:
            return -1
        if city_finish in cities:
            return iter + 1

    copy_cities = cities.copy()
    copy_cities.remove(city_start)

    next_cities = []
    iter += 1

    for city in cities:
        distance = abs(int(city[0]) - int(city_start[0])) + abs(
            int(city[1]) - int(city_start[1])
        )
        if distance <= max_distance:
            x = find_city(city, city_finish, copy_cities, iter)
            all_cities.append(x)
    print(all_cities)
    return max(all_cities)


copy_cities = cities.copy()
copy_cities.remove(city_start)
iter = 1

next_cities = []
for city in copy_cities:
    distance = abs(int(city[0]) - int(city_start[0])) + abs(
        int(city[1]) - int(city_start[1])
    )
    if distance <= max_distance:
        next_cities.append(city)


queue = [(city_start, next_cities, 0)]

while queue:
    st, n, i = queue.pop()

    if city_finish in next_cities:
        print(i + 1)

    else:
        for city in copy_cities:
            distance = abs(int(city[0]) - int(city_start[0])) + abs(
                int(city[1]) - int(city_start[1])
            )
            if distance <= max_distance:
                nx = n.copy()
                nx.remove(city)
                queue.append(
                    city,
                    nx,
                )


print(-1)


iter += 1
