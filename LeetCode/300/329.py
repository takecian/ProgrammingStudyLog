class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ans = 0
        if len(matrix) == 0:
            return 0

        h = len(matrix)
        w = len(matrix[0])

        visited = [[False] * w for _ in range(h)]

        def dfs(si, sj):
            length = 0
            que = [(si, sj, 1)]
            while que:
                i, j, l = que.pop()
                length = max(length, l)
                current = matrix[i][j]
                for di, dj in zip([1, 0, -1, 0], [0, 1, 0, -1]):
                    neigbor_i = i + di
                    neigbor_j = j + dj
                    if 0 <= neigbor_i < h and 0 <= neigbor_j < w and current < matrix[neigbor_i][neigbor_j]:
                        visited[neigbor_i][neigbor_j] = True
                        que.append((neigbor_i, neigbor_j, l + 1))
            return length

        for i in range(h):
            for j in range(w):
                if visited[i][j]:
                    continue
                current = matrix[i][j]
                can_start = True
                for di, dj in zip([1, 0, -1, 0], [0, 1, 0, -1]):
                    neigbor_i = i + di
                    neigbor_j = j + dj

                    if 0 <= neigbor_i < h and 0 <= neigbor_j < w and current > matrix[neigbor_i][neigbor_j]:
                        can_start = False
                        break
                if can_start:
                    print('{} {}'.format(i, j))
                    visited[i][j] = True
                    ans = max(ans, dfs(i, j))
        return ans