class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        element = -101
        lag = 0

        for e, n in enumerate(nums):
            if n != element:
                nums[e - lag] = n
                element = n

            else:
                lag += 1

        return len(nums) - lag

 # leetcode solution


 # 1 1 1 2 2 3

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i,j=0,1
        while i<=j and j<len(nums):
            if nums[i]==nums[j]:
                j+=1
            else:
                nums[i+1]=nums[j]
                i+=1
        return i+1