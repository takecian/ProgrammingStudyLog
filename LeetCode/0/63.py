class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        H = len(obstacleGrid)
        W = len(obstacleGrid[0])

        grid = [[0] * W for _ in range(H)]

        if obstacleGrid[0][0] == 0:
            grid[0][0] = 1

        for i in range(1, H):
            if obstacleGrid[i][0] == 0:
                grid[i][0] = grid[i - 1][0]

        for j in range(1, W):
            if obstacleGrid[0][j] == 0:
                grid[0][j] = grid[0][j - 1]

        for i in range(1, H):
            for j in range(1, W):
                if obstacleGrid[i][j] == 1:
                    continue
                grid[i][j] = grid[i - 1][j] + grid[i][j - 1]

        return grid[-1][-1]



