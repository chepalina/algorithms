"""
Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.



Example 1:

Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.
Example 2:

Input: n = 1, k = 1
Output: [[1]]
Explanation: There is 1 choose 1 = 1 total combination.
"""

# 12 13 14 23 24 34

GLOBAL_LIST = []


def combine(n, k):
    nums = range(1, n + 1)
    backtracking([], nums, k)


def backtracking(l, nums, k):
    print("call ", l, nums, k)

    if len(l) == k:
        GLOBAL_LIST.append(l.copy())
        return

    for i in range(len(nums)):
        l.append(nums[i])
        temp = nums[i + 1 :]
        backtracking(l, temp, k)
        l.pop()


combine(4, 2)
print(GLOBAL_LIST)

# [] [1234]
# [1] []234
# [23] [34]

# [1] [34]
# [1] [4]

# [2] [34]

GLOBAL_LIST = []
combine(1, 1)
print(GLOBAL_LIST)


print("# ------------- Iterations")


# ------------- Iterations

from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def generate(elements, num):
            curr_i = list(range(num))
            while True:
                print(elements, curr_i)
                yield [elements[i] for i in curr_i]

                for idx in reversed(range(num)):
                    if curr_i[idx] != idx + len(elements) - num:
                        break
                else:
                    return

                curr_i[idx] += 1

                for j in range(idx + 1, num):
                    curr_i[j] = curr_i[j - 1] + 1
                    print("count")

        return [t for t in generate(list(range(1, n+1)), k)]


s = Solution()
print(s.combine(4, 2))