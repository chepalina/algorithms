"""https://leetcode.com/problems/search-insert-position/"""



class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while  right != left:
            middle = (right + left)//2
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

print(s.searchInsert(nums = [1,3,5,6], target = 5), 2 )
print(s.searchInsert(nums = [1,3,5,6], target = 2), 1 )
print(s.searchInsert(nums = [1,3,5,6], target = 7), 4 )







