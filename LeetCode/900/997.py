from collections import defaultdict


class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        trusted_count = [0] * N
        truster_count = [0] * N
        for truster, trusted in trust:
            trusted_count[trusted - 1] += 1
            truster_count[truster - 1] += 1

        ans = []
        for n in range(N):
            if trusted_count[n] == N - 1 and truster_count[n] == 0:
                ans.append(n + 1)

        return ans[0] if len(ans) == 1 else -1