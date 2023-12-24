# from itertools import zip_longest
#
# a = "111"
# b = "1100"
#
# for x,y in zip_longest(a, b, fillvalue="0"):
#     print(x,y)
#
#
# print(list(range(1,5)))


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # "0" "0" -> "0"
        # "1" "0" -> "1"
        # "1" "1" -> "10"
        # "11" "11" -> "110"
        # "111" "0" -> "111"
        # "111" "111" -> "1110
        # "111" "1000" -> "1111
        # "1000" "1000" -> "10000

        target_str = ""
        add = 0

        common_index = min(len(a), len(b))

        for i in range(1, common_index + 1):

            target_int = int(a[-i]) + int(b[-i]) + add
            if target_int == 0:
                target_str = "0" + target_str
                add = 0
            elif target_int == 1:
                target_str = "1" + target_str
                add = 0
            elif target_int == 2:
                target_str = "0" + target_str
                add = 1
            elif target_int == 3:
                target_str = "1" + target_str
                add = 1

        remainder_str = a if len(a) > len(b) else b

        for i in range(common_index + 1, max(len(a), len(b)) + 1):
            target_int = int(remainder_str[-i]) + add
            if target_int == 0:
                target_str = "0" + target_str
                add = 0
            elif target_int == 1:
                target_str = "1" + target_str
                add = 0
            elif target_int == 2:
                target_str = "0" + target_str
                add = 1

        if add == 1:
            target_str = "1" + target_str

        return target_str


class Solution1:
    def addBinary(self, a: str, b: str) -> str:
        # "0" "0" -> "0"
        # "1" "0" -> "1"
        # "1" "1" -> "10"
        # "11" "11" -> "110"
        # "111" "0" -> "111"
        # "111" "111" -> "1110
        # "111" "1000" -> "1111
        # "1000" "1000" -> "10000

        target = ""
        add = 0

        a, b = a[::-1], b[::-1]

        # прибавляем 1 для обработки последнего значения
        for i in range(max(len(a), len(b))):
            sum = (
                add
                + (int(a[i]) if i < len(a) else 0)
                + (int(b[i]) if i < len(b) else 0)
            )

            target += str(1 if sum % 2 != 0 else 0)
            add = sum // 2

        if add:
            target += "1"

        return target[::-1]


s = Solution1()


# print( '"0" "0" -> "0" actual ', s.addBinary("0","0"))
# print( '"1" "0" -> "1" actual ', s.addBinary("1","0"))
print('"1" "1" -> "10" actual ', s.addBinary("1", "1"))
print('"11" "11" -> "110" actual ', s.addBinary("11", "11"))
print('"111" "0" -> "111" actual ', s.addBinary("111", "0"))
print('"111" "111" -> "1110 actual ', s.addBinary("111", "111"))
print('"111" "1000" -> "1111 actual ', s.addBinary("111", "1000"))
print('"1000" "1000" -> "10000 actual ', s.addBinary("1000", "1000"))
