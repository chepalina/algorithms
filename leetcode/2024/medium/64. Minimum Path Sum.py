from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        dp = [[0]*(n+1) for _ in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                if i == 1:
                    dp[i][j] = grid[i-1][j-1] + dp[i][j-1]
                elif j == 1:
                    dp[i][j] = grid[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = grid[i-1][j-1] + min(dp[i-1][j], dp[i][j-1])

        return dp[m][n]


class Solution2:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        dp = [[0]*n for _ in range(m)]

        for i in range(n):
            dp[0][i] = grid[0][i] + ( 0 if i==0 else dp[0][i-1])

        for i in range(m):
            dp[i][0] = grid[i][0] + (0 if i==0 else dp[i-1][0])

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])

        return dp[m-1][n-1]


s = Solution2()
s.minPathSum(grid = [[1,2,3],[4,5,6]])
