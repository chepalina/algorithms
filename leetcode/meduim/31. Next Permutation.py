#
#
# nums = [1,2,3]
# print(nums[-1])
# for i in range(len(nums)-1, -1,-1):
#     print(i)



from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 1 1 5
        # 1 5 1
        # 5 1 1

        # 0 1 5. 1 2 5
        # 0 5 1. 1 5 2
        # 1 0 5. 2 1 5
        # 1 5 0. 2 5 1
        # 5 0 1  5 1 2
        # 5 1 0. 5 2 1

        # 1 2 3
        # 1 3 2
        # 2 1 3
        # 2 3 1
        # 3 1 2
        # 3 2 1


        decrease_index = len(nums)-1
        for i in range(len(nums)-2, -1, -1):
            print(decrease_index)
            if nums[decrease_index] <= nums[i]:
                decrease_index = i

        if decrease_index - 1 >= 0:
            val = nums[decrease_index - 1]
            min_val = val
            min_index = len(nums) -1
            for i in range(decrease_index, len(nums), 1):
                if nums[i] - val < min_val:
                    min_val = nums[i] - val
                    min_index = i

            nums[decrease_index - 1], nums[min_index] = nums[min_index], nums[decrease_index - 1]

        index_counter = -1
        for i in range(decrease_index, (len(nums)+decrease_index)//2):
            nums[i], nums[index_counter] = nums[index_counter], nums[i]

        print(nums)


s = Solution().nextPermutation(nums = [1,2,3])
print("Expected: [1,3,2]")

s = Solution().nextPermutation( nums = [3,2,1])
print("Expected: [1,2,3]")

s = Solution().nextPermutation( nums = [1,1,5])
print("Expected: [1,5,1]")






