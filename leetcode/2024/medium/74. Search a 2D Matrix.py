from typing import List


class Solution:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        matrix_len = len(matrix) * len(matrix[0])

        left = 0
        right = matrix_len - 1

        while left <= right:

            middle = (right + left) // 2

            middle_i = middle // len(matrix)
            middle_j = middle % len(matrix)

            middle_el = matrix[middle_i][middle_j]
            if middle_el == target:
                return True

            if middle_el > target:
                right = middle - 1
            else:
                left = middle + 1

        return False


s = Solution()

assert s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]] , 3) is True
assert s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]] , 13) is False