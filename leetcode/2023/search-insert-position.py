"""https://leetcode.com/problems/search-insert-position/


Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104

"""


class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while right != left:
            middle = (right + left) // 2
            middle_element = nums[middle]

            if middle_element == target:
                return middle - 1 + 1

            if middle_element > target:
                right = middle - 1

            if middle_element < target:
                left = middle + 1

        last_element = nums[right]

        if last_element > target:
            return right - 1

        if last_element < target:
            return right + 1


s = Solution()

print(s.searchInsert(nums=[1, 3, 5, 6], target=5), 2)
print(s.searchInsert(nums=[1, 3, 5, 6], target=2), 1)
print(s.searchInsert(nums=[1, 3, 5, 6], target=7), 4)
