from collections import deque


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        H = len(matrix)
        if H == 0:
            return 0
        W = len(matrix[0])
        if W == 0:
            return 0

        def is_min(h, w):
            val = matrix[h][w]
            for dh, dw in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                if 0 <= h + dh < H and 0 <= w + dw < W:
                    if val > matrix[h + dh][w + dw]:
                        return False
            return True

        def get_bigger_neigbors(h, w):
            ret = []
            val = matrix[h][w]
            for dh, dw in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                if 0 <= h + dh < H and 0 <= w + dw < W:
                    if val < matrix[h + dh][w + dw]:
                        ret.append((h + dh, w + dw))
            return ret

        ans = 0
        visited = set()
        for h in range(H):
            for w in range(W):
                if (h, w) in visited:
                    continue
                if not is_min(h, w):
                    continue

                # bfs
                que = deque()
                que.append((h, w, 1))
                while que:
                    ch, cw, path = que.popleft()
                    ans = max(ans, path)
                    visited.add((ch, cw))
                    for next_h, next_w in get_bigger_neigbors(ch, cw):
                        que.append((next_h, next_w, path + 1))

        return ans