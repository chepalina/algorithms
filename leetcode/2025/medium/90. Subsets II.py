from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        def backtrack(start_ind, curr, res):
            res.append(curr[:])

            print(curr)

            for loop_ind in range(start_ind, len(nums)):
                if loop_ind > start_ind and nums[loop_ind] == nums[loop_ind - 1]:
                    continue

                curr.append(nums[loop_ind])
                backtrack(loop_ind + 1, curr, res)
                curr.pop()

        backtrack(0, [], result)
        return result


s = Solution()

print(s.subsetsWithDup(nums=[2, 2, 2]) )  # == [[], [2], [2, 2], [2, 2, 2]]

assert s.subsetsWithDup(nums=[1, 2, 2]) == [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
