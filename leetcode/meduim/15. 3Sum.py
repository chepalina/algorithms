from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # [-1 -2 -3] -> []
        # [-1 0 1 -1 0 1 -1 0 1] -> [-1 0 1]
        # [-1 0 1 -2 2] -> [-1 0 1] [-2 0 2]

        # 2 - 1 +
        # 2+ 1-
        # 1+ 1- 0
        # 0 0 0

        negative = []
        pozitive = []
        zero = []

        target = []

        for i in nums:
            if i > 0:
                pozitive.append(i)
            elif i < 0:
                negative.append(i)
            else:
                zero.append(i)

        print(zero, pozitive, negative)

        pozitive.sort()
        negative.sort()

        # 0 0 0
        if len(zero) >= 3:
            target.append([0, 0, 0])
        # 1+ 1- 0
        if len(zero) >= 1:
            for n in negative:
                for p in pozitive:
                    temp = [n, 0, p]
                    if n + p == 0 and temp not in target:
                        target.append(temp)

        # 2+ 1-
        # [1 2 3] - 12 13 23
        for p1_i in range(len(pozitive)):
            for p2_i in range(p1_i + 1, len(pozitive)):
                for n in negative:
                    if pozitive[p1_i] + pozitive[p2_i] + n == 0:
                        temp = [pozitive[p1_i], pozitive[p2_i], n]
                        if temp not in target:
                            target.append(temp)

        for n1_i in range(len(negative)):
            for n2_i in range(p1_i + 1, len(negative)):
                for p in pozitive:
                    if negative[n1_i] + negative[n2_i] + p == 0:
                        temp = [negative[n1_i], negative[n2_i], p]
                        if temp not in target:
                            target.append(temp)

        return target


s = Solution()


print(s.threeSum([-1, 0, 1, 2, -1, -4]))
