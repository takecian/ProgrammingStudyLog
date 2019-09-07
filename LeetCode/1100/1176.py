class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        n = len(calories)
        ans = 0
        total = sum(calories[:k])
        if total > upper:
            ans += 1
        if total < lower:
            ans -= 1

        for i in range(k, n):
            total += calories[i]
            total -= calories[i-k]
            if total > upper:
                ans += 1
            if total < lower:
                ans -= 1
        return ans