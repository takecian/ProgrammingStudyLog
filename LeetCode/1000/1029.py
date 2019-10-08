class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs) // 2

        diff_cost = list(map(lambda c: (c[0], c[1], c[0] - c[1]), costs))
        # print(diff_cost)
        diff_cost.sort(key=lambda x: x[2])
        return sum(map(lambda c: c[0], diff_cost[:n])) + sum(map(lambda c: c[1], diff_cost[n:]))