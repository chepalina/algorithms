class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []

        candidates.sort()

        def rec(curr, i):

            if sum(curr) > target:
                return

            if sum(curr) == target and curr not in res:
                res.append(curr.copy())

            for i in range(i, len(candidates)):
                c_temp = curr.copy()
                c_temp.append(candidates[i])
                rec(c_temp, i + 1)

        for i in range(len(candidates)):
            rec([candidates[i]], i + 1)

        return res
