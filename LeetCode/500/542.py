from collections import deque


class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        height = len(matrix)
        width = len(matrix[0])

        ans = [[0] * width for _ in range(height)]

        for h in range(height):
            for w in range(width):
                if matrix[h][w] == 0:
                    continue
                # search nearest 0
                ans[h][w] = self.bfs(height, width, h, w, matrix)
        return ans

    def bfs(self, height, width, h, w, mat):
        dhs = [0, 1, 0, -1]
        dws = [1, 0, -1, 0]

        que = deque()
        que.append((h, w, 0))
        neigbor_min = 10 * 9
        while que:
            h, w, d = que.popleft()
            for dh, dw in zip(dhs, dws):
                new_h = h + dh
                new_w = w + dw
                if 0 <= new_h < height and 0 <= new_w < width:
                    if mat[new_h][new_w] == 0:
                        return d + 1
                    else:
                        que.append((new_h, new_w, d + 1))
        return -1