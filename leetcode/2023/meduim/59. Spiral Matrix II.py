from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # 4

        # 1 2 3  4
        # 12 13 14 5
        # 11 16 15 6
        # 10 9 8 7

        row = [0] * n
        target = [row.copy() for _ in range(n)]

        i, j = 0, -1

        for val in range(1, n**2+1):
            i, j = self.get_next((i, j), target, n)
            target[i][j] = val

        return target

    def get_next(self, index, target, n):
        i, j = index

        # вправо
        if j + 1 < n and target[i][j + 1] == 0:
            return i, j + 1

        # вниз
        if i + 1 < n and target[i + 1] [j] == 0:
            return i + 1, j

        # влево
        if j-1 < n and target[i] [j-1] == 0:
            return i, j - 1

        # вверх
        # if i - 1 < n and target[i - 1][j] == 0:
        return i - 1, j


# s = Solution()
# print(s.generateMatrix(3))
#
# assert s.generateMatrix(3) == [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
# assert s.generateMatrix(1) == [[1]]


class SolutionOptimal:
    def generateMatrix(self, n: int) -> List[List[int]]:

        target = [[0]*n for _ in range(n)]

        left, right = 0, n-1
        top, bottom = 0, n-1
        value = 1

        while left <= right:

            for c in range(left, right+1):
                target[top][c] = value
                value += 1
            top += 1

            for c in range(top, bottom+1):
                target[c][right] = value
                value +=1
            right -= 1

            for c in range(right, left-1, -1):
                target[bottom][c] = value
                value +=1
            bottom -= 1

            for c in range(bottom, top-1, -1):
                target[c][left] = value
                value +=1
            left += 1

        return target


s = SolutionOptimal()
print(s.generateMatrix(3))

assert s.generateMatrix(3) == [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
assert s.generateMatrix(1) == [[1]]

