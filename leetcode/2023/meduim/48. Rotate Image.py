from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # 1 -> i[1][1] -> i[3][1]
        # 2 -> i[2][1] -> i[3][2]
        # 3 -> i[3][1] -> i[3][3]

        # 2 -> i[2][1] -> i[3][2]
        # 5 -> i[2][2] -> i[2][2]
        # 8 -> i[2][3] -> i[1][2]

        # reverse
        # l = 0
        # r = len(matrix) -1
        # while l < r:
        #     matrix[l], matrix[r] = matrix[r], matrix[l]
        #     l += 1
        #     r -= 1

        matrix.reverse()

        print(matrix)

        # transpose
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


s = Solution()
m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
s.rotate(matrix=m)
print(m)

# [[7, 8, 9], [4, 5, 6], [1, 2, 3]]
# [[7, 4, 1], [8, 5, 2], [9, 6, 3]]


# [[7,4,1],[8,5,2],[9,6,3]]
