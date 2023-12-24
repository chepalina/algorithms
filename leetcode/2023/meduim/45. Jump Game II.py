# https://www.youtube.com/watch?v=dJ7sWiOoK7g
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:

        res = 0
        l = r = 0

        futherest = 0

        while r < len(nums) - 1:
            for index in range(l, r + 1):
                futherest = max(futherest, index + nums[index])

            l = r + 1
            r = futherest
            res += 1

        return res


class SolutionDP:
    def jump(self, nums: List[int]) -> int:
        dp = [0] * len(nums)

        # первый элемент предрасчитан (занимает 0 шагов) и еще -1 потому что индекс
        for index in range(len(nums) - 2, -1, -1):
            temp_dp = 1001
            for dp_index in range(index + 1, min(index + nums[index] + 1, len(nums))):
                temp_dp = min(temp_dp, dp[dp_index])

            dp[index] = temp_dp + 1

        return dp[0]


s = SolutionDP()

assert s.jump([2, 3, 0, 3, 4]) == 2
