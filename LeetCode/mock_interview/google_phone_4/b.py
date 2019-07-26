from collections import Counter

class Solution(object):
    def knightProbability(self, N, K, r, c):
        memo = {}
        moves = ((-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2))
        def dfs(k, x, y, P):
            p = 0
            if 0 <= x < N and 0 <= y < N: #a valid position on the board
                if k < K:
                    for dx, dy in moves:
                        x_next, y_next = x + dx, y + dy
                        if (x_next, y_next, k+1) not in memo:
                            memo[(x_next, y_next, k+1)] = dfs(k+1, x_next, y_next, P/8)
                        p += memo[(x_next, y_next, k+1)]
                else: # k==K, this is the last move
                    p = P
            return p
        return dfs(0, r, c, 1.0)