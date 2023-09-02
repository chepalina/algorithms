class MySolution:
    def climbStairs(self, n: int) -> int:

        # 1 -> 1
        # 2 -> 2
        # 3 -> 3
        # 4 - > 5

        stairs = {1: 1, 2: 2}

        for i in range(1, n + 1):
            answer = stairs.get(i)
            if answer is None:
                answer = stairs.get(i - 1) + stairs.get(i - 2)
                stairs[i] = answer

        return stairs.get(n)


print(MySolution().climbStairs(20))


class Solution(object):
    def climbStairs(self, n):

        if n <= 2:
            return n

        a, b, c = 0, 1, 2

        while n > 2:
            a, b = b, c
            c = a + b
            n = n - 1

        return c


print(Solution().climbStairs(20))
