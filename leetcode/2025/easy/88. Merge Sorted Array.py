from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return

        first = m -1
        second = n -1
        end = m+n-1

        while second >=0:

            if first < 0 or nums1[first] < nums2[second]:
                nums1[end] = nums2[second]
                second -= 1

            else:

                nums1[end] = nums1[first]
                first -= 1

            end -= 1

        print(nums1)



s = Solution()
s.merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)


s.merge(nums1 = [-1,0,1,0,0,0], m = 3, nums2 = [-2,5,6], n = 3)