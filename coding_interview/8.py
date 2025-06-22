# Recursion & dynamic
# ---------------8.1------------------------


# 1 = 1
# 2 = 2
# 3 = (2, 1, 0) = 4 - ?
# 4 = (3, 2, 1) = 1+2+4 + 1 -? = 7
# 5 = 2 + 4 + 7 = 13


def count_ways(n: int) -> int:
    if n < 3:
        return n

    temp1 = 1  # 0 steps - it is easier to define ot to 1 then 0
    temp2 = 1  # 1 step
    temp3 = 2  # 2 step

    for i in range(3, n + 1):
        ways = temp1 + temp2 + temp3
        temp1, temp2, temp3 = temp2, temp3, ways

    return temp3


assert count_ways(5) == 13


# ---------------8.2------------------------
# grid


def get_path(maze: list) -> list:
    if not maze:
        return []

    path = []
    failed_points = set()
    create_path(maze, path, failed_points, len(maze) - 1, len(maze[0]) - 1)
    return path


def create_path(maze: list, path: list, failed_points: set, row: int, col: int) -> bool:
    if col < 0 or row < 0 or not maze[row][col]:
        return False

    p = (row, col)

    if p in failed_points:
        return False

    is_origin = p == (0, 0)

    if (
        is_origin
        or create_path(maze, path, failed_points, row - 1, col)
        or create_path(maze, path, failed_points, row, col - 1)
    ):
        path.append(p)
        return True

    failed_points.add(p)
    return False


maze_ex = [[1, 0, 1], [1, 1, 1], [1, 0, 1]]

print(get_path(maze_ex))

# ---------------8.3------------------------
# magic index

ex = [-5, -4, -1, 3, 5, 10, 15]
ex1 = [0]


def find_magic_distinct(magic_list: list) -> int:
    l, r = 0, len(magic_list) - 1

    while l <= r:
        m = (l + r) // 2
        if magic_list[m] == m:
            return m

        if magic_list[m] < m:
            l = m + 1
        elif magic_list[m] > m:
            r = m - 1

    return -1


print(find_magic_distinct(ex))

ex2 = [3, 3, 3, 3]


def find_magic(magic_list: list) -> int:
    def magic(array, s, e):
        if e < s:
            return -1

        m = (s + e) // 2
        if array[m] == m:
            return m

        # return max(magic(array, s, min(m-1, magic_list[m])),
        #            magic(array, max(m + 1, magic_list[m]), e))

        left = magic(array, s, min(m - 1, magic_list[m]))
        if left > 0:
            return left

        right = magic(array, max(m + 1, magic_list[m]), e)

        return right

    return magic(magic_list, 0, len(magic_list) - 1)


print(find_magic(ex2))

# ---------------8.4------------------------
# power set


i_set = ["a", "b", "c"]


def power_set(set_: list) -> list:

    def get_subsets(s, index) -> list:
        if len(s) == index:
            return [set()]
        else:
            all_subsets = get_subsets(s, index + 1)
            item = s[index]
            extra_subsets = []

            for subset in all_subsets:
                new_subset = subset.copy()
                new_subset.add(item)
                extra_subsets.append(new_subset)

            all_subsets.extend(extra_subsets)

        return all_subsets

    return get_subsets(set_, 0)


# print("SUBSETS")
print(power_set(i_set))

import copy


def power_set_iter(set_: list) -> list:

    result = [set()]

    for element in set_:
        result_copy = copy.deepcopy(result)

        for r in result_copy:
            r.add(element)

        result.extend(result_copy)

    return result


# print("SUBSETS")
# print(power_set_iter(i_set))


def power_set_bin(set_: list) -> list:
    def convert_bin_to_set(bin_value):
        res = set()
        index = 0
        while bin_value > 0:
            if (bin_value & 1) == 1:
                res.add(set_[index])
            index += 1
            bin_value = bin_value >> 1

        return res

    result = []
    max_num = 2 ** len(set_)  # 1 << len(set_)

    for n in range(max_num):
        subset = convert_bin_to_set(n)
        result.append(subset)

    return result


print(power_set_bin(i_set))


# ---------------8.5------------------------
# recursive multiply


def multiply(a: int, b: int) -> int:
    smaller = a if a < b else b
    bigger = a if a > b else b

    return multiply_recursive(smaller, bigger)


def multiply_recursive(smaller: int, bigger: int) -> int:
    if smaller == 0:
        return 0

    if smaller == 1:
        return bigger

    m = smaller >> 1
    half = multiply_recursive(m, bigger)

    if smaller % 2 > 0:
        return half + half + bigger

    return half + half


def multiply_rec_not_optimal(smaller: int, bigger: int) -> int:
    if smaller == 0:
        return 0

    if smaller == 1:
        return bigger

    return multiply_recursive(smaller - 1, bigger) + bigger


print(multiply_rec_not_optimal(4, 12))


# ---------------8.6------------------------
# towers


def move_tower(discs: list):
    first = discs
    second = []
    third = []
    print(first, second, third)

    def move_disc(quantity: int, origin: list, destination: list, buffer: list):

        if quantity <= 0:
            return

        move_disc(
            quantity - 1, origin, buffer, destination
        )  # move top from origin to buffer
        disc = origin.pop()  # move top from origin to destination
        if destination and destination[-1] < disc:
            print(f"error! {disc=} cannot added to {destination[-1]}")
        destination.append(disc)
        move_disc(
            quantity - 1, buffer, destination, origin
        )  # move top from buffer to dest

    move_disc(len(discs), first, third, second)
    return first, second, third


print(move_tower([3, 2, 1]))


# ---------------8.7------------------------
# permutations without dups


def create_permutations_loop(string: str) -> list[str]:
    if not string:
        return []

    res = [string[0]]

    def gen(result: list, letter: str):
        temp = result.copy()
        result = []

        for t in temp:
            for i in range(len(t) + 1):
                new = t[0:i] + letter + t[i:]
                result.append(new)

        return result

    for s in range(1, len(string)):
        res = gen(res, string[s])

    return res


assert set(create_permutations_loop("abc")) == {
    "cba",
    "bca",
    "bac",
    "cab",
    "acb",
    "abc",
}


def create_perm_recursive(string: str) -> list[str]:
    def gen(first, second, result) -> list[str]:
        if not second:
            result.append(first)

        for i in range(len(second)):
            before = second[0:i]
            after = second[i + 1 :]
            cur = second[i]
            gen(first + cur, before + after, result)

        return result

    res = []
    return gen("", string, res)


assert set(create_perm_recursive("abc")) == {"cba", "bca", "bac", "cab", "acb", "abc"}


# ---------------8.8------------------------
# permutations with dups


def perms_with_dups(string: str) -> list[str]:
    letter_map = dict()
    result = []

    for s in string:
        letter_map[s] = letter_map.get(s, 0) + 1

    gen_perms(letter_map, "", len(string), result)

    return result


def gen_perms(l_map: dict, first: str, remaining: int, result: list):
    if remaining == 0:
        result.append(first)
        return

    for k, v in l_map.items():
        if v > 0:
            l_map[k] = v - 1
            gen_perms(l_map, first + k, remaining - 1, result)
            l_map[k] = v


print(perms_with_dups("aab"))


# ---------------8.9------------------------
# parens
# 1 ()
# 2 ()() (())
# 3 ()()() ()(()) (())() (()()) ((()))


def generate_parens(n: int) -> list:

    def backtracking(pref: str, left: int, right: int, result: list):

        if right < left or left < 0:
            return

        if left == 0 and right == 0:
            res.append(pref)
        else:
            pref += "("
            backtracking(pref, left - 1, right, result)

            pref = pref[0 : len(pref) - 1] + ")"
            backtracking(pref, left, right - 1, result)

    res = []
    backtracking("", n, n, res)
    return res


print(generate_parens(3))


# ---------------8.10------------------------
# paint fill
# 1 1 1 2
# 2 1 1 1
# 2 2 1 1

screen_ex = [[1, 1, 1, 2], [2, 1, 1, 1], [2, 2, 1, 1]]


def fill_screen(screen: list, pixel: tuple, color: int):
    col, row = pixel
    old_colour = screen[col][row]
    if old_colour == color:
        return screen

    def recurse(screen: list, pixel: tuple, color_old: int, color_new: int):
        col, row = pixel

        if screen[col][row] != color_old:
            return

        screen[col][row] = color_new
        if row - 1 >= 0:
            recurse(screen, (col, row - 1), color_old, color_new)
        if row + 1 < len(screen[0]):
            recurse(screen, (col, row + 1), color_old, color_new)
        if col - 1 >= 0:
            recurse(screen, (col - 1, row), color_old, color_new)
        if col + 1 < len(screen):
            recurse(screen, (col + 1, row), color_old, color_new)

    recurse(screen, pixel, old_colour, color)
    return screen


assert fill_screen(screen_ex, (2, 0), 3) == [[1, 1, 1, 2], [3, 1, 1, 1], [3, 3, 1, 1]]


# ---------------8.11------------------------
# coins


def calculate_coins(n: int) -> int:
    # 1/2
    # 7 -> 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    #      0  1  2  2  3  3  4  4  5  5  6
    #4 -> 1 1 1 1 / 1 1 2/ 2 2
    #6 -> 111111/11112/1122/222
    #10 1111111111/111111112/11111122/1111222/112222/22222

    dp = [0]*(n+1)
    dp[1] = 1

    for i in range(2,n+1):
        # обработка единички
        dp[i] = dp[i-1]

        if i%5==0:
            dp[i] += 1
        if i%10==0:
            dp[i] += 1
        if i%25==0:
            dp[i] += 1

    return dp[-1]


assert calculate_coins(5) == 2


denoms = [1,5,10,15]


def make_change(n: int, denoms: list):
    dp =[0]* len(denoms)
    dp = [dp.copy() for _ in range((n+1))]

    def rec(total: int, denoms: list, index: int, dp_map: list):
        if dp_map[total][index] > 0:
            return dp_map[total][index]

        coin = denoms[index]
        if index == len(denoms) - 1:
            r = total%coin
            return 1 if r == 0 else 0

        num_of_ways, amount = 0, 0

        while amount <= total:
            num_of_ways += rec(total-amount, denoms, index+1, dp_map)
            amount+=coin

        dp_map[total][index] = num_of_ways
        return num_of_ways

    return rec(n, denoms, 0, dp)


print(calculate_coins(50), make_change(50, denoms))


# ---------------8.12------------------------
# queens



def place_queens():
    grid_size = 8

    def check_valid(columns: list, row1: int, col1: int):
        for row2 in range(row1):

            col2 = columns[row2]
            if col1 == col2:
                return False

            if abs(col2-col1) == row1-row2:
                return False

        return True

    def place(row: int, columns: list, results: list):
        if row == grid_size:
            results.append(columns[:])

        else:
            for col in range(grid_size):
                if check_valid(columns, row, col):
                    columns[row] = col
                    place(row+1, columns, results)

    result = []
    columns = [0]*grid_size
    place(0, columns, result)
    print(result)


place_queens()








# ---------------8.13------------------------
# boxes
from dataclasses import dataclass
from typing import Optional

@dataclass
class Box:
    height: int
    weight: int
    depth: int

    def can_be_above(self, oth: "Box"):
        return self.height < oth.height and self.weight < oth.weight and self.depth < oth.depth


boxes_ex = [Box(1,1,1), Box(2,2,2), Box(5,5,5), Box(2,2,2)]


def create_stack(boxes: list):
    boxes.sort(key=lambda b: b.height, reverse=True)
    print(boxes)
    stack_map = [0]*len(boxes)

    def rec(boxes: list["Box"], bottom: Optional["Box"], offset: int, stack_map: list):
        if offset >= len(boxes):
            return 0

        new_bottom = boxes[offset]
        height_with = 0
        if bottom is None or new_bottom.can_be_above(bottom):
            if stack_map[offset] == 0:
                stack_map[offset] = rec(boxes, new_bottom, offset + 1, stack_map)
                stack_map[offset] += new_bottom.height

            height_with = stack_map[offset]

        height_without = rec(boxes, bottom, offset+1, stack_map)

        return max(height_with, height_without)

    res = rec(boxes, None, 0, stack_map)
    print(stack_map)
    return res


print(create_stack(boxes_ex))


# ---------------8.13------------------------
# bool evaluation


def eval_bool(s: str, res: bool, memo: dict ) -> int:
    if not s: return 0
    if len(s) == 1: return 1 if bool(s=="1") == res else 0
    if memo.get((res, s)) is not None: return memo[(res, s)]

    ways = 0
    for i in range(1, len(s), 2):
        left = s[0:i]
        right = s[i+1:]
        left_true = eval_bool(left, True, memo)
        left_false = eval_bool(left, False, memo)
        right_true = eval_bool(right, True, memo)
        right_false = eval_bool(right, False, memo)
        total = (left_true+left_false)*(right_true+right_false)

        c = s[i]
        total_true = 0
        if c == "^":
            total_true = (left_true*right_false) + (left_false*right_true)
        if c == "&":
            total_true = left_true*right_true
        if c == "|":
            total_true = (left_true*right_true) + (left_false*right_true) + (left_true*right_false)

        total_false = total-total_true
        sub_ways = total_true if res else total_false
        ways += sub_ways


    memo[(res, s)] = ways
    return ways


print("---------------------------")


s = "1^0|0|1"
memo = {}
assert eval_bool("1^0|0|1", False, memo) == 2
assert eval_bool("0&0&0&1^1|0", True, memo) == 10





