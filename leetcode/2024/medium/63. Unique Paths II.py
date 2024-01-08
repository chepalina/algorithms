class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        if obstacleGrid[m - 1][n - 1] == 1:
            return 0

        # dp = [[0]*n for _ in range(m)]

        _temp_obstacle = 1
        for i in range(n):
            _temp_obstacle = min(0 if obstacleGrid[0][i] == 1 else 1, _temp_obstacle)
            obstacleGrid[0][i] = _temp_obstacle

        _temp_obstacle = 1
        for j in range(1, m):
            _temp_obstacle = min(0 if obstacleGrid[j][0] == 1 else 1, _temp_obstacle)
            obstacleGrid[j][0] = _temp_obstacle

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                else:
                    obstacleGrid[i][j] = obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1]

        print(obstacleGrid)

        return obstacleGrid[m - 1][n - 1]

