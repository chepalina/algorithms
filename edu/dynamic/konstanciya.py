# C. Аппарат Констанции
# https://codeforces.com/problemset/problem/1245/C?locale=ru

# ouuokarinn -> 4
# banana -> 1
# nnn -> 3
# amanda -> 0
# nnnan -> 3


def count_strings(string: str):

    if "w" in string or "m" in string:
        return 0

    target_num = 1

    count = 0
    prev_symbol = string[0]

    for s in string:
        if s not in ("u", "n") or prev_symbol != s:
            if count > 1:
                target_num *= fib_count(count)
            count = 1
        else:  # prev_symbol == s:
            count += 1

        prev_symbol = s

    if count > 1:
        target_num *= fib_count(count)

    return target_num


def fib_count(num: int):
    if num == 1:
        return 1
    if num == 2:
        return 2

    first = 1
    second = 2

    for _ in range(3, num + 1):
        first, second = second, first + second

    return second


assert count_strings("nnn") == 3, count_strings("nnn")
assert count_strings("ouuokarinn") == 4, count_strings("ouuokarinn")
