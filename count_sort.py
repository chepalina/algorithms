"""Сортировка подсчетом"""


from xml.dom import minicompat


x = [1, 5, 3, 9, 2, 4, 11]


def sort(input_list: list) -> list:
    max_element = input_list[0]
    min_element = input_list[0]

    for e in input_list:
        if e > max_element:
            max_element = e
        if e < min_element:
            min_element = e

    count = [0] * (max_element + min_element)
    print(count)

    for e in input_list:
        index = e - min_element
        count[index] += 1

    print(count)

    sorted = []
    for num, el in enumerate(count):
        if el > 0:
            sorted.append(min_element + num)

    return sorted


print(sort(x))


x = [1, 3, 2]

min_e, max_e = min(x), max(x)
cnt = [0] * (max_e - min_e + 1)
for v in x:
    cnt[v - min_e] += 1
k = 0
for i in range(len(cnt)):
    for c in range(cnt[i]):
        x[k] = i + min_e
        k += 1

print(" ".join(map(str, x)))
