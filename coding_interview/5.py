# 5.1


def insert(n, m, i, j):
    # сделать маску для очистки битов от i до j
    mask = "0b" + "1" * (len(bin(n)) - 2)
    print(mask)
    mask_bin = int(mask, 2)
    left = mask_bin << (j + 1)
    print(format(left, "32b"))
    right = (1 << i) - 1
    print(format(right, "32b"))

    mask2 = left | right
    print(bin(mask2))

    n_cleared = n & mask2
    print(bin(n_cleared))
    m_shifted = m << i
    print(bin(m_shifted))

    result = n_cleared | m_shifted
    print(bin(result))


# clear bit example
# def clearBit(int_type, offset):
#     mask = ~(1 << offset)
#     return(int_type & mask)
#
# print(bin(clearBit(0b10000000, offset=5)))


# x = 0b10000000000
# y = 0b10011
# insert(x, y, 2, 6)


# ----------------------------------------------------


def binary_to_string(num: float):

    if 1 <= num <= 0:
        return "ERROR"

    binary = "0."

    while num > 0:

        if (
            len(binary) > 32
        ):  # Ограничение длины строки для предотвращения бесконечного цикла
            return "ERROR"

        num *= 2

        if num >= 1:
            binary += "1"
            num -= 1
        else:
            binary += "0"

        print(num, binary)

    return binary


# print(binary_to_string(0.625))


# 5.3 ----------------------------------------------------


s = "11011101111"

s1 = "00000"


def flip_bit_str(string: str):

    zero_i_first = 0
    zero_i_next = 0
    max_len = 0

    for i in range(len(string)):

        if string[i] == "0":
            zero_i_first = zero_i_next
            zero_i_next = i

        max_len = max(max_len, i - zero_i_first)

    if zero_i_first == 0:
        max_len += 1

    return max_len


assert flip_bit_str(s) == 8
assert flip_bit_str("111") == 3
assert flip_bit_str("00000") == 1


def flip_bit(a: int):
    if ~a == 0:
        return a.bit_length()

    cur_len = 0
    prev_len = 0
    max_len = 1
    while a != 0:
        if (a & 1) == 1:
            cur_len += 1
        else:
            prev_len = 0 if (a & 2) == 0 else cur_len
            cur_len = 0

        max_len = max(prev_len + cur_len + 1, max_len)
        # Преобразуем значение в 32-битное беззнаковое число
        a &= 0xFFFFFFFF
        # Выполняем сдвиг вправо
        a = (a >> 1) & 0xFFFFFFFF

    return max_len


assert flip_bit(1775) == 8


# 5.4 ----------- GET NEXT----------------


def get_next(n: int) -> int:
    c = n
    c0 = 0
    c1 = 0

    while ((c & 1) == 0) and (c != 0):
        c0 += 1
        c = c >> 1

    while (c & 1) == 1:
        c1 += 1
        c = c >> 1

    p = c0 + c1
    print(f"bit n = {bin(n)}, p={p}")
    if p == 31 or p == 0:
        return -1

    print(f"n | (1 << p) {bin(n)} | {bin(1 << p)}")
    n = n | (1 << p)
    n = n & ~((1 << p) - 1)
    n = n | (1 << (c1 - 1)) - 1

    return n


print(get_next(4))



def get_prev(n: int) -> int:
    c = n
    c0 = 0
    c1 = 0

    while (c & 1) == 1:
        c1 += 1
        c = c >> 1

    if c == 0:
        return -1

    while ((c & 1) == 0) and (c != 0):
        c0 += 1
        c = c >> 1

    p = c0 + c1
    n = n & (~0) << (p + 1)
    mask = (1 << (c1 + 1)) - 1
    n = n | mask << (c0 - 1)

    return n



print(get_prev(145))


def get_next_arith(n: int) -> int:
    c = n
    c0 = 0
    c1 = 0

    while ((c & 1) == 0) and (c != 0):
        c0 += 1
        c = c >> 1

    while (c & 1) == 1:
        c1 += 1
        c = c >> 1

    p = c0 + c1


# print(bin(4 + (2**2-1)))


# 5.6

# example
# 29 - 11101 15 - 01111 -> 2

def get_conversion(a: int, b: int) -> int:

    if a == b:
        return 0

    z = a ^ b
    res = 0

    while z != 0:
        print(bin(z), z & 1)
        res += z & 1
        z = z >> 1
        print(bin(z))

    return res


print("5.6------------------")
assert get_conversion(29, 15) == 2


# 5.7 swap
print("5.7------------------")
print(bin(0xaaaaaaaa), bin(0x55555555))


def swap(n: int):
    return ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1)


# print(bin(100))
# print(bin(100 & 0xaaaaaaaa))
# print(bin(100 & 0x55555555))
# print(bin(swap(100)))

print("5.8------------------")

def draw_line(screen: list, width: int, x1: int, x2: int, y: int):
    pass

print(bin(0XFF))








