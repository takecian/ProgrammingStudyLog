class Solution:
    def mergeStones(self, stones: List[int], K: int) -> int:
        def calc_merge_cost(i, j, piles):
            if i == j:
                return 0
            if (i, j, piles) in dp:
                return dp[(i, j, piles)]
            if piles == 1:
                dp[(i, j, piles)] = calc_merge_cost(i, j, K) + pre_sum[j + 1] - pre_sum[i]
                return dp[(i, j, piles)]
            else:
                min_cost = float('inf')
                for k in range(i, j, K - 1):
                    min_cost = min(min_cost, calc_merge_cost(i, k, 1) + calc_merge_cost(k + 1, j, piles - 1))
                dp[(i, j, piles)] = min_cost
                return dp[(i, j, piles)]

        n = len(stones)
        if K > 2 and n % (K - 1) != 1:
            return -1

        pre_sum = [0] * (n + 1)
        for i in range(n):
            pre_sum[i + 1] = pre_sum[i] + stones[i]

        dp = {}
        return calc_merge_cost(0, n - 1, 1)