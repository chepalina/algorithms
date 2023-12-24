from typing import List


class Solution:
    # 8,0,1,2,4,5,6,7
    # 6,7,8,0,1,2,4,5

    def findMin(self, nums: List[int]) -> int:

        if nums[0] < nums[-1]:
            return nums[0]

        l = 0
        r = len(nums) - 1

        m = (l + r) // 2

        while r - l > 1:
            if nums[m] > nums[r]:
                l = m
            else:
                r = m

            m = (l + r) // 2

        return nums[r]


s = Solution()

assert s.findMin(nums=[3, 4, 5, 1, 2]) == 1
