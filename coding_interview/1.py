# Arrays and strings


# 1.1


def check_unique(string):
    str_map = {}
    for s in string:
        str_map[s] = str_map.get(s, 0) + 1

    for value in str_map.values():
        if value > 1:
            return True

    return False


assert check_unique(string="11123485") == True
assert check_unique(string="12345") == False


# 1.2


def check_permutation(string1, string2):

    if len(string1) != len(string2):
        return False

    str_map1 = {}
    str_map2 = {}
    for s1, s2 in zip(string1, string2):
        str_map1[s1] = str_map1.get(s1, 0) + 1
        str_map2[s2] = str_map2.get(s2, 0) + 1

    # for v in str_map.values():
    #     if v != 0:
    #         return False

    return str_map1 == str_map2


assert check_permutation(string1="aaa", string2="aaa") == True
assert check_permutation(string1="abc", string2="cba") == True
assert check_permutation(string1="abcc", string2="cba") == False
assert check_permutation(string1="qwert", string2="trewd") == False
assert check_permutation(string1="", string2="") == True
# useful thing  - print(ord("z"))

# 1.3


def replace_string_inplace(string, length):
    target = [s for s in string]

    position_index = len(target) - 1

    for i in range(length - 1, -1, -1):
        if target[i] != " ":
            target[position_index] = target[i]
            position_index -= 1
        else:
            (
                target[position_index],
                target[position_index - 1],
                target[position_index - 2],
            ) = ("0", "2", "%")
            position_index -= 3

    return "".join(target)


assert (
    replace_string_inplace("Mr John Smith    ", 13) == "Mr%20John%20Smith"
), replace_string_inplace("Mr John Smith    ", 13)


# 1.4
def check_palindrome_permutation(string: str):
    s_map = {}
    for s in string:
        if s.isalpha():
            s = s.lower()
            s_map[s] = s_map.get(s, 0) + 1

    counter = 0
    for v in s_map.values():
        if v % 2 > 0:
            counter += 1
            if counter > 1:
                return False

    return True


# 1.6
def compress(string: str):

    if not string:
        return ""

    counter = 1
    prev = string[0]
    target = ""

    for i in range(1, len(string)):
        if string[i] == prev:
            counter += 1
        else:
            target += f"{prev}{counter}"
            prev = string[i]
            counter = 1

    target += f"{prev}{counter}"
    return target if len(target) < len(string) else string


assert compress("aaabbbccc") == "a3b3c3", compress("aaabbbccc")
assert compress("arrrrrrt") == "a1r6t1"
assert compress("") == ""
assert compress("abc") == "abc"


# 1.7
# example
# [[1,2,3],   00-02  01-12  02-22
# [4,5,6],    10-01  11-11  12-21
# [7,8,9]]    20-00  21-10  22-20
#   ->
# [[7,4,1],
# [8,5,2],
# [9,6,3]]


def rotate_matrix(matrix: list[list]) -> list[list]:

    for row_index in range(len(matrix)):
        for col_index in range(row_index, len(matrix)):
            matrix[row_index][col_index], matrix[col_index][row_index] = (
                matrix[col_index][row_index],
                matrix[row_index][col_index],
            )

    for row_index in range(len(matrix)):
        for col_index in range(len(matrix) // 2):
            (
                matrix[row_index][col_index],
                matrix[row_index][len(matrix) - 1 - col_index],
            ) = (
                matrix[row_index][len(matrix) - 1 - col_index],
                matrix[row_index][col_index],
            )

    return matrix


m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

assert rotate_matrix(m) == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]


def zero_matrix(matrix: list[list]) -> list[list]:
    set_row = set()
    set_col = set()

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                set_row.add(i)
                set_col.add(j)

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):

            if i in set_row or j in set_col:
                matrix[i][j] = 0

    return matrix


m = [[1, 2, 3], [4, 0, 6], [7, 8, 9]]

# print(zero_matrix(m))


# 1.9

def check_string_rotation(s1, s2):
    if len(s1) != len(s2):
        return False

    temp = s1+s1
    return s2 in temp



assert check_string_rotation("watterbottle", "terbottlewat") is True
assert check_string_rotation("watterbottle", "terbottlwat") is False
assert check_string_rotation("watterbottl", "terbottlewat") is False

