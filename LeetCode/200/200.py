from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        height = len(grid)
        width = len(grid[0])
        for i in range(height):
            for j in range(width):
                if grid[i][j] == '1':
                    ans += 1
                    que = deque()
                    que.append((i,j))
                    while que:
                        h, w = que.pop()
                        grid[h][w] = '0'
                        for dh, dw in zip([0, 1, 0, -1], [1, 0, -1, 0]):
                            neigbor_h = h + dh
                            neigbor_w = w + dw
                            if 0 <= neigbor_w < width and 0 <= neigbor_h < height:
                                if grid[neigbor_h][neigbor_w] == '1':
                                    que.append((neigbor_h, neigbor_w))
        return ans