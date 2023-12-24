from typing import List


class SolutionPointers:

    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        target = 0
        result = []
        prev = None

        for i, num in enumerate(nums):

            if num == prev:
                continue

            if num > target:
                break

            two_sum_target = target - num
            two_sum_result = self.two_sum(nums, i+1, two_sum_target)

            result.extend([[num]+r for r in two_sum_result])

            prev = num

        return result

    def two_sum(self, nums: list, index:int, target: int):

        left = index
        right = len(nums) - 1
        result = []
        prev = None

        while left < right:

            if prev == nums[left]:
                left += 1
                continue

            if nums[left] + nums[right] == target:
                result.append([nums[left], nums[right]])
                right -= 1

            elif nums[left] + nums[right] < target:
                left += 1

            elif nums[left] + nums[right] > target:
                right -= 1

            prev = nums[left]

        return result



s = SolutionPointers()

# r = s.threeSum(nums = [-1,0,1,2,-1,-4])
#
assert s.threeSum(nums = [-1,0,1,2,-1,-4]) == [[-1,-1,2],[-1,0,1]]
assert s.threeSum(nums = [0,1,1]) == []
assert s.threeSum(nums = [0,0,0]) == [[0,0,0]]
assert s.threeSum(nums = [0,0,0,0,0,0,0,0]) == [[0,0,0]]



class SolutionHashMap:

    def threeSum(self, nums: List[int]) -> List[List[int]]:

        result = set()
        target = 0
        seen = set()

        for index, num in enumerate(nums):
            if num in seen:
                continue

            two_sum_target = target - num

            two_sum_result: set[list[int]] = self.two_sum(nums, index+1, two_sum_target)
            for r in two_sum_result:
                res = [num] + list(r)
                res.sort()
                result.add(tuple(res))

            seen.add(num)

        return result


    def two_sum(self, nums, index, target) -> set[list[int]]:
        result = set()
        hashmap = {}

        for i in range(index, len(nums)):

            second_num_index = hashmap.get(nums[i])

            if second_num_index is not None:
                pair = [nums[i], nums[second_num_index]]
                result.add(tuple(pair))

            hashmap[target-nums[i]] = i

        return result



s = SolutionHashMap()

d = s.threeSum(nums = [-1,0,1,2,-1,-4])
e = s.threeSum(nums = [0,0,0])


assert s.threeSum(nums = [-1,0,1,2,-1,-4]) == {tuple(e) for e in [[-1,-1,2],[-1,0,1]]}
assert s.threeSum(nums = [0,1,1]) == set()
assert s.threeSum(nums = [0,0,0]) == {(0,0,0)}
assert s.threeSum(nums = [0,0,0,0,0,0,0,0]) == {(0,0,0)}













class Solution:
    # сложное решение
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


