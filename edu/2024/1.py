# Задача A. Двоичный поиск


def bin_search(sorted_list: list, num: int) -> bool:
    if not sorted_list or num < sorted_list[0] or num > sorted_list[-1]:
        return False

    l, r = 0, len(sorted_list) - 1
    m = (l + r) // 2

    while l <= r:

        if sorted_list[m] == num:
            return True

        elif sorted_list[m] > num:
            r = m - 1

        elif sorted_list[m] < num:
            l = m + 1

        m = (l + r) // 2

    return False


assert bin_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], -2) is False
assert bin_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0) is False
assert bin_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 4) is True
assert bin_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 9) is True
assert bin_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 12) is False
assert bin_search([1, 2, 3, 4, 6, 7, 8, 9, 10], 5) is False


# Задача B. Рядом


def find_min_abs(sorted_list: list, num: int) -> int:
    if sorted_list and num < sorted_list[0]:
        return sorted_list[0]

    l, r = 0, len(sorted_list) - 1
    m = (l + r) // 2

    while l <= r:

        if sorted_list[m] == num:
            return num

        elif sorted_list[m] < num:
            l = m + 1

        elif sorted_list[m] > num:
            r = m - 1

        m = (l + r) // 2

    # min_left_el = r

    if len(sorted_list) - 1 > r + 1:
        return (
            sorted_list[r + 1]
            if abs(sorted_list[r] - num) > abs(sorted_list[r + 1] - num)
            else sorted_list[r]
        )

    return sorted_list[r]


assert find_min_abs([1, 3, 5, 7, 9], 2) == 1
assert find_min_abs([1, 3, 5, 7, 9], 4) == 3
assert find_min_abs([1, 3, 5, 7, 9], 8) == 7
assert find_min_abs([1, 3, 5, 7, 9], 1) == 1
assert find_min_abs([1, 3, 5, 7, 9], 6) == 5

# Задача C. Отгадай число

from random import randint


def get_num(n: int):
    x = randint(1, n)
    print(x)
    return x


def guess(n: int, target: int) -> None:
    l, r = 1, n
    m = (l + r) // 2

    while m != target:
        print(m)

        if target > m:
            l = m + 1
        else:
            r = m - 1

        m = (l + r) // 2

    print(m)


guess(100, get_num(100))

# Задача D. Квадратный корень и квадратный квадрат
from math import sqrt


def bin_search(c: float) -> float:
    l, r = 0, c

    m = (l + r) / 2

    while abs(m ** 2 + sqrt(m + 1) - c) > pow(10, -6):

        if l > r:
            print(l, r)

        if m ** 2 + sqrt(m + 1) > c:
            r = m - pow(10, -6)
        else:
            l = m + pow(10, -6)

        m = (l + r) / 2

    return m


print(bin_search(2))

assert abs(bin_search(2) - 0.80926547401163950735) < 1e-6
assert abs(bin_search(18) - 3.97119409286392421876) < 1e-6


# Задача E. Корень кубического уравнения


def solve_cubic(a, b, c, d):
    eps = pow(10, -14)

    f = lambda x: a * pow(x, 3) + b * pow(x, 2) + c * x + d

    r = 1
    while f(r) * f(-r) >= 0:
        r *= 2

    l = -r

    while r - l > eps:
        x = (l + r) / 2

        if f(x) * f(r) > 0:
            r = x
        else:
            l = x

    return l


print(solve_cubic(1, -3, 3, -1))


# Задача F. Сортировка слиянием с приколом

list_example = [6, 11, 18, 28, 31]


inv_count = 0
def merge_sort(arr):
    if len(arr) > 1:
        # Нахождение середины массива
        mid = len(arr) // 2
        # Деление элементов на 2 половины
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Рекурсивный вызов сортировки для каждой половины
        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        # Копирование данных в временные массивы L[] и R[]
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
                global inv_count
                inv_count += (mid - i)
            k += 1

        # Проверка, остались ли элементы в L[]
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Проверка, остались ли элементы в R[]
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr

# Пример использования
example_array = [12, 11, 13, 5, 6, 7]
list_example = [6, 11, 18, 28, 31]
list_example1 = [1, 3, 2, 4]

sorted_array = merge_sort(example_array)
print(sorted_array, inv_count)



def list_inversions(arr):
    inversions = []
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                inversions.append((arr[i], arr[j]))
    return inversions

# Пример использования
example_array = [12, 11, 13, 5, 6, 7]
inversions = list_inversions(example_array)
print("Inversions:")
for inv in inversions:
    print(inv)
