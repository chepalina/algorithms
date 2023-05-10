from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # [2 2 2 2 2] 8 -> [2 2 2 2]

        result = set()

        nums.sort()

        for i in range(len(nums) - 1):
            if i > 0 and nums[i] == nums[i-1]:
                print("continue")
                continue

            for j in range(i+1, len(nums)):
                l = j+1
                r = len(nums) - 1

                while l < r:
                    # print(nums[i] ,nums[j] , nums[l] , nums[r])
                    sum_ = nums[i] + nums[j] + nums[l] + nums[r]
                    if sum_ == target:
                        result.add((nums[i], nums[j], nums[l], nums[r]))
                        l += 1
                    elif sum_ > target:
                        r -= 1
                    else:
                        l += 1

        return result





s = Solution()

print(s.fourSum(nums = [1,0,-1,0,-2,2], target = 0))
print(s.fourSum(nums = [2,2,2,2,2], target = 8))