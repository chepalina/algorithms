class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        quotient = 0
        sum_ = 0

        remainder = (2**31-1 if divisor > 1 else -2**31) - sum_

        while sum_ < dividend and ((remainder > divisor and divisor > 0) or (remainder < divisor and divisor < 0)):
            quotient += 1
            sum_ += divisor
            remainder -= divisor

            print(remainder, divisor)

        if sum_ > dividend:
            return quotient - 1

        return quotient

class Solution1:
    def divide(self, dividend: int, divisor: int) -> int:

        quotient = 0
        sum_ = 0

        if dividend == 0:
            return 0

        if divisor == -2**31:
            return 1 if dividend == -2**31 else 0

        dividend_sign = -1 if dividend < 0 else 1

        if divisor >0 and dividend> 0:
            sign = 1
        elif divisor <0 and dividend>0:
            sign = -1
        elif divisor >0 and dividend<0:
            sign = -1
        elif divisor <0 and dividend<0:
            sign = 1

        remainder = 2**31-1 if sign > 0 else -2**31

        while (dividend > 0 and dividend_sign == 1) or (dividend < 0 and dividend_sign == -1):
            if dividend > 0:
                dividend -= abs(divisor)
            else:
                dividend += abs(divisor)

            # print(dividend)

            quotient += 1



        return quotient - 1 if sign == 1 else -quotient + 1



#
# s = Solution1()
#
# print(s.divide(dividend = 10, divisor = 3))
# print(s.divide(dividend = 7, divisor = -3))

dividend = 555
divisor = 7

multiple = 1
while dividend >= (divisor << 1):
    divisor <<= 1
    multiple <<= 1

    print(dividend, divisor)


print(100>>2)