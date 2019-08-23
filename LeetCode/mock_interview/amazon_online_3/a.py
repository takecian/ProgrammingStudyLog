from collections import Counter
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        dominoes = list(map(lambda d: (d[0], d[1]) if d[0] < d[1] else (d[1], d[0]), dominoes))
        dominoes.sort(key=lambda d: (d[0], d[1]))
        c = Counter(dominoes)
        ans = 0
        for v in c.values():
            if v > 1:
                ans += v * (v-1)//2
        return ans