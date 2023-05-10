from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        middle = (left + right) // 2

        while left != right:

            if nums[middle] == target:
                return middle

            elif nums[middle] > target:
                right = middle - 1

            elif  nums[middle] < target:
                left = middle + 1

            middle = (left + right) // 2


        if nums[middle] == target:
            return middle
        if nums[middle] > target:
            return middle - 1
        elif nums[middle] < target:
            return middle + 1




print( "[1,3,5,6], 2) -> expected 1 -> actual ", Solution().searchInsert([1,3,5,6], 2))
print( "[1,3,5,6], 5) -> expected 2 -> actual ", Solution().searchInsert([1,3,5,6], 5))
print( "[1,3,5,6], 7) -> expected 4 -> actual ", Solution().searchInsert([1,3,5,6], 7))
print( "[1,3,5,6], 0) -> expected 0 -> actual ", Solution().searchInsert([1,3,5,6], -1))
print( "[1,3,5,6], 1) -> expected 0 -> actual ", Solution().searchInsert([1,3,5,6], 1))
