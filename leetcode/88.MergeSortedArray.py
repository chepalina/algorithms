from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # [1 1 1] [] -> [1 1 1]
        # [0 0] [1 5] -> [1 5]
        # [1 4 7 0 0] [2 3] -> [1 2 3 4 7]
        # [1 3 7 0 0] [2 4] -> [1 2 3 4 7]

        # [] [] -> []
        # [ 0 1 3 0 0] [0 0] -> [0 0 0 1 2 3]
        # [5 6 7 0 0 0] [8 9 10] -> [5 6 7 8 9 10]
        # [4 4 0 0] [1 2] -> [1 2 4 4]
        # [-10 -8 0 0] [1 2] -> [-10 -8 1 2]

        target_index = m + n - 1

        while n > 0:

            if m == 0:
                nums1[target_index] = nums2[n - 1]
                n -= 1
                target_index -= 1
                continue

            element1 = nums1[m - 1]
            element2 = nums2[n - 1]

            if element1 > element2:
                nums1[target_index] = element1
                m -= 1
            else:
                nums1[target_index] = element2
                n -= 1

            target_index -= 1


s = Solution()


nums = [1, 1, 1]
s.merge([1, 1, 1], 3, [], 0)
assert nums == [1, 1, 1], nums

nums = [0, 0]
s.merge(nums, 0, [1, 5], 2)
assert nums == [1, 5], nums
