#
#
# print("2**31-> ",(2**31-1))
#
print((2 ** 31 - 1) ** 0.5)
print(46340 ** 2)
print(2 ** 31 - 1)
#


class Solution:
    def mySqrt(self, x: int) -> int:
        # 1 -> 1
        # 2 -> 1
        # 3 -> 1
        # 4 -> 2
        # 9 -> 3

        if x == 0:
            return 0
        if x == 1:
            return 1

        left = 0
        right = x

        while left <= right:
            middle = (left + right) // 2

            if middle * middle == x:
                return middle
            elif middle * middle > x:
                right = middle - 1
            elif middle * middle < x:
                left = middle + 1

        return right

        # 11 -> l=0 r=11 m=5 25 > 11

    # l=0 r=4 m =2 4 < 11 ->
    # l=3 r=4 m=3 9<11 ->
    # l=4 r=4 m=4 16>11 ->
    # l=4 r=3


s = Solution()

assert s.mySqrt(9) == 3, s.mySqrt(9)
assert s.mySqrt(8) == 2, s.mySqrt(8)
assert s.mySqrt(11) == 3, s.mySqrt(11)
assert s.mySqrt(2 ** 31 - 1) == 46340, s.mySqrt(2 ** 31 - 1)


class Solution1:
    def mySqrt(self, x: int) -> int:
        # 1 -> 1
        # 2 -> 1
        # 3 -> 1
        # 4 -> 2
        # 8 -> 2
        # 9 -> 3

        # 11 -> 3

        left = 0
        right = x

        while left <= right:
            middle = (right + left) // 2

            square = middle * middle

            if square == x:
                return middle

            if square > x:
                right = middle - 1

            elif square < x:
                left = middle + 1

        return right

    # 5 l=0 r=5 m=2 -> 4 < 5 l=3 r=5 m=4 16>5 l=3 r=3 m=3  9>5 r=2


s = Solution1()

assert s.mySqrt(11) == 3, s.mySqrt(11)
assert s.mySqrt(1) == 1, s.mySqrt(1)
