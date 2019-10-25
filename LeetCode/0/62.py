# https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0] * m for _ in range(n)]
        for i in range(n):
            grid[i][0] = 1

        for j in range(m):
            grid[0][j] = 1

        for i in range(1, n):
            for j in range(1, m):
                grid[i][j] = grid[i - 1][j] + grid[i][j - 1]

        return grid[-1][-1]
