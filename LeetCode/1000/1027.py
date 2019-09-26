class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = [collections.defaultdict(int) for _ in A]
        res = 1
        for i in range(len(A)):
            for j in range(i):
                v = A[i] - A[j]
                dp[i][v] = dp[j][v] + 1
                res = max(dp[i][v], res)
        return res+1