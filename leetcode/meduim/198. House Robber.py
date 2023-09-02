from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:

        rob0, rob1 = 0, 0

        for e in nums:
            temp = max(rob0 + e, rob1)
            rob0, rob1 = rob1, temp

        return rob1







    def rob_3_vars(self, nums: List[int]) -> int:

        if len(nums) <= 2:
            return max(nums)

        n_3, n_2, n_1 = nums[0], nums[1], nums[2] + nums[0]

        for i in range(3, len(nums)):
            current_max = max(nums[i] + n_2, nums[i] + n_3)
            n_3, n_2, n_1 = n_2, n_1, current_max

        return max(n_2, n_1)



    def rob_list(self, nums: List[int]) -> int:

        if len(nums) <= 2:
            return max(nums)

        _temp = [nums[0], nums[1], nums[2] + nums[0]]

        for i in range(3, len(nums)):
            current_max = max(nums[i] + _temp[i-2], nums[i] + _temp[i-3])
            _temp.append(current_max)

        return max(_temp[-1], _temp[-2])



s = Solution()

assert s.rob([10,1,1,10]) == 20

