from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        target = []
        dict_nums = {}
        perm = []

        for n in nums:
            el_count = dict_nums.get(n, 0)
            dict_nums[n] = el_count+1

        print(dict_nums)

        def dfs():
            if len(perm) == len(nums):
                target.append(perm.copy())
                return

            for element, count in dict_nums.items():
                print(element, count)
                if count > 0:
                    perm.append(element)
                    dict_nums[element] -= 1

                    dfs()

                    perm.pop()
                    dict_nums[element] += 1

        dfs()

        return target

s = Solution()
print(s.permute([1,1,3]))







