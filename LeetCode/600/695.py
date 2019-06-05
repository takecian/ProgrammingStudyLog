
import itertools
from collections import Counter
from collections import defaultdict
import bisect
from heapq import heappush, heappop

class Solution:
    def maxAreaOfIsland(self, grid):

        def draw(i, j):
            if 0 <= i < len(grid) and 0 <= i < len(grid[i]):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    area = 1
                    dx4 = [0, 0, 1, -1]
                    dy4 = [1, -1, 0, 0]

                    for dx, dy in zip(dx4, dy4):
                        area += draw(i + dx, j + dy)

                    return area
                else:
                    return 0
            else:
                return 0
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    ans = max(ans, draw(i, j))

        return ans

def main():
    grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
    s = Solution()
    print((s.maxAreaOfIsland(grid)))


if __name__ == '__main__':
    main()
