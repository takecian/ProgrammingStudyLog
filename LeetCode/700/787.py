class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        dp = [100000] * n
        dp[src] = 0

        for k in range(K + 1):
            next_dp = [dp[i] for i in range(n)]
            # print(k)
            for s, d, p in flights:
                next_dp[d] = min(next_dp[d], dp[s] + p)
            # print(next_dp)
            dp = next_dp
        ans = dp[dst]
        return ans if ans != 100000 else -1
