from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # n * (n-1) * (n-2)

        max_amount = 0
        for first_num, first_el in enumerate(height):
            for second_num, second_el in enumerate(height):
                length = min(first_el, second_el)
                width = second_num - first_num
                max_amount = max(max_amount, length*width)

        return max_amount

    def maxAreaPointers(self, height: List[int]) -> int:

        l=0
        r=len(height)-1
        max_amount = 0

        while l != r:
            min_height = min(height[l], height[r])
            max_amount = max(max_amount, (r-l)*min_height)

            if height[l] < height[r]:
                l += 1
            else:
                r += 1

        return max_amount



