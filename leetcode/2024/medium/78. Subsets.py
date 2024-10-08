# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

from typing import List


GLOBAL_LIST = []

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtracking(left, right):
            GLOBAL_LIST.append(left.copy())

            if not right:
                return

            for i in range(len(right)):
                left.append(right[i])
                backtracking(left, right[i+1:])
                left.pop()

        backtracking([], nums)


s = Solution()
s.subsets(nums = [1,2,3])
print(GLOBAL_LIST)
GLOBAL_LIST.sort()
res = [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
res.sort()

assert GLOBAL_LIST == res