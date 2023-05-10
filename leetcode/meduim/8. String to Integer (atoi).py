class Solution:
    def myAtoi(self, s: str) -> int:
        # "" -> 0
        # "1.2" -> "1"
        # "333_=." -> "333"
        # "..._+_   654" -> 0
        # " ++ 654" -> 0
        # "-1" -> -1
        # "-    1" -> 0
        # "1 6" -> 1

        sign = None
        target = 0
        breakpoint_ = False

        digits = '0123456789'

        for element in s:
            if element == " " and not breakpoint_:
                continue

            if element == "+" and not sign:
                digsignit = 1
                continue
            elif element == "-" and not sign:
                sign = -1
                continue
            elif element in "+-" and sign:
                return 0

            if element not in digits:
                break
            else:
                breakpoint_ = True
                target = target*10 + int(element)

            if target > 2**31:
                return 0

        target = target * (sign or 1)
        if target > 2**31 - 1 or target < -2**31:
            return 0

        return target





s = Solution()

assert s.myAtoi("") == 0
assert s.myAtoi("1.2") == 1
assert s.myAtoi("333_=.") == 333
assert s.myAtoi("..._+_   654") == 0
assert s.myAtoi("-1") == -1
assert s.myAtoi("     -1") == -1, s.myAtoi("     -1")
assert s.myAtoi("1 6" ) == 1, s.myAtoi("1 6" )