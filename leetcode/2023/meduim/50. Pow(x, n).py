class Solution:
    def myPow(self, x: float, n: int) -> float:

        if x == 0:
            return 0

        if n == 0:
            return 1

        mid = abs(n) // 2
        remainder = x if abs(n) % 2 > 0 else 1

        half = self.myPow(x, mid)

        if n < 0:
            half = 1 / half
            remainder = 1 / remainder

        return half * half * remainder


s = Solution()


assert s.myPow(x=2.00000, n=10) == 1024.00000
assert s.myPow(x=2.1, n=3) == 9.261000000000001, s.myPow(x=2.1, n=3)
assert s.myPow(x=2.00000, n=-2) == 0.25
