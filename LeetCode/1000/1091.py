class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # BFS
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0

        H = len(grid)
        W = len(grid[0])

        visited = [[False] * W for _ in range(W)]
        if grid[0][0] == 1:
            return -1
        que = [(0, 0, 1)]
        visited[0][0] = True

        ans = -1
        while que:
            h, w, path = que.pop(0)
            if h == H - 1 and w == W - 1:
                ans = path
                break
            for dh, dw in zip([-1, -1, -1, 0, 0, 1, 1, 1], [-1, 0, 1, -1, 1, -1, 0, 1]):
                next_h = h + dh
                next_w = w + dw
                if 0 <= next_h < H and 0 <= next_w < W and grid[next_h][next_w] == 0 and not visited[next_h][next_w]:
                    que.append((next_h, next_w, path + 1))
                    visited[next_h][next_w] = True

        return ans