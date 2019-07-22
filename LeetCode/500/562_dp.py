# https://leetcode.com/problems/longest-line-of-consecutive-one-in-matrix/
class Solution(object):
    def longestLine(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        if not M:
            return 0

        H = len(M)
        W = len(M[0])

        dp = [[[0, 0, 0, 0] for _ in range(W)] for _ in range(H)]

        def get_val_if_range(h, w, i):
            if 0 <= h < H and 0 <= w < W:
                return dp[h][w][i]
            else:
                return 0

        ans = 0
        for h in range(H):
            for w in range(W):
                if M[h][w] == 1:
                    # vertical
                    dp[h][w][0] = get_val_if_range(h - 1, w, 0) + 1
                    # horizontal
                    dp[h][w][1] = get_val_if_range(h, w - 1, 1) + 1
                    # diagonal
                    dp[h][w][2] = get_val_if_range(h - 1, w - 1, 2) + 1
                    # anti-diagonal
                    dp[h][w][3] = get_val_if_range(h - 1, w + 1, 3) + 1
                # print(dp[h][w])
                ans = max(ans, max([v for v in dp[h][w]]))

        return ans