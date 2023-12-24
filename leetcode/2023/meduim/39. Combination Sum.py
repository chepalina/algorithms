from typing import List


# норм solution
# https://www.youtube.com/watch?v=GBKI9VSKdGg


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []

        def rec(i, curr):

            curr_sum = sum(curr)

            if curr_sum == target:
                res.append(curr.copy())
                return

            if curr_sum > target:
                return

            if i == len(candidates):
                return

            curr_cp = curr.copy()
            curr_cp.append(candidates[i])
            rec(i, curr_cp)

            rec(i + 1, curr)

        rec(0, [])

        return res


class Solution:
    def __init__(self):
        self.TARGET_RES = set()

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        # 2 3 6 -> 3 2 6 23 36 26 236 # 1 3 7
        # 2 3 6 1 -> 23 26 21 36 31 61

        res_candidates = set()

        for i in candidates:
            res_candidates.add(self.backtrack([i], candidates, target))

        print(self.TARGET_RES)

        return [list(i) for i in self.TARGET_RES]

    def backtrack(self, current, candidates, target):

        sum_ = sum(current)

        if sum_ == target:
            current.sort()
            self.TARGET_RES.add(tuple(current))
            return

        if sum_ > target:
            return

        if sum_ < target:
            for i in candidates:
                c = current.copy()
                c.append(i)
                self.backtrack(c, candidates, target)


s = Solution()
# s.combinationSum(candidates = [2,3,6,7], target = 7)

assert s.combinationSum(candidates=[2, 3, 6, 7], target=7) == [[2, 2, 3], [7]]
s = Solution()
assert s.combinationSum(candidates=[2, 3, 5], target=8) == [
    [2, 2, 2, 2],
    [2, 3, 3],
    [3, 5],
]


s = Solution()
assert s.combinationSum(candidates=[2], target=1) == []


"""The complexity of the provided code can be analyzed as follows:

Let N be the length of the candidates list and T be the target value.

The combinationSum function iterates through each element in the candidates list once, resulting in a time complexity of O(N).
Within the backtrack function, a recursive call is made for each candidate in the candidates list. The number of recursive calls can vary depending on the structure of the input and the target value.
In the worst case scenario, where all possible combinations sum up to the target, the number of recursive calls can be exponential, resulting in a time complexity of O(2^N).
However, in practice, the actual number of recursive calls is often much lower, as branches are pruned when the current sum exceeds the target value.
The TARGET_RES set is used to store the unique combinations, with duplicate combinations being filtered out due to the set's nature. The conversion of the set to a list has a complexity of O(len(TARGET_RES)).
The space complexity of the code is influenced by the recursion stack and the storage of combinations in the TARGET_RES set.
In the worst case scenario, where all possible combinations sum up to the target, the space complexity can be exponential, O(2^N).
However, in practice, the actual space usage is often much lower, as the set filters out duplicate combinations and the recursion stack size is limited by the depth of the recursive calls.
In summary, the time complexity is O(N * 2^N) in the worst case, and the space complexity is O(2^N) in the worst case.
"""
