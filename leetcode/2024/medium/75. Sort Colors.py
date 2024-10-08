from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        r = 0
        w = 0
        b = len(nums) - 1

        while w <= b:
            if nums[w] == 0:
                nums[r], nums[w] = nums[w], nums[r]
                w += 1
                r += 1

            elif nums[w] == 1:
                w += 1
            else:
                nums[w], nums[b] = nums[b], nums[w]
                b -= 1


s = Solution()

ex1 = [2, 0, 2, 1, 1, 0]
s.sortColors(ex1)
assert ex1 == [0, 0, 1, 1, 2, 2]

ex2 = [2, 0, 1]
s.sortColors(ex2)
assert ex2 == [0, 1, 2]
