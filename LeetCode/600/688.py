class Solution(object):
    def knightProbability(self, N, K, r, c):
        dp = [[0] * N for _ in xrange(N)]
        moves = ((-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2))
        dp[r][c] = 1

        for _ in xrange(K):
            dp2 = [[0] * N for _ in xrange(N)]
            for ri in range(N):
                for ci in range(N):
                    val = dp[ri][ci]
                    for dr, dc in moves:
                        next_r = ri + dr
                        next_c = ci + dc
                        if 0 <= next_r < N and 0 <= next_c < N:
                            dp2[next_r][next_c] += val / 8.0
            dp = dp2

        return sum(map(sum, dp))

