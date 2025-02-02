class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 4:
            return n

        temp1 = 1
        temp2 = 2

        for i in range(3, n + 1):
            temp1, temp2 = temp2, temp1+temp2

        return temp2