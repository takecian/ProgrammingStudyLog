
class Solution:
    def solve(self, current, candidates, target):
        ans = []
        if target == 0:
            ans.append(current)
        if target < 0:
            return []
        for c in candidates:
            li = self.solve(current + [c], candidates, target - c)
            for l in li:
                if len(l) > 0:
                    ans.append(l)
        return ans

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        for c in candidates:
            li = self.solve([c], candidates, target - c)
            for l in li:
                if len(l) > 0:
                    l.sort()
                    if l not in ans:
                        ans.append(l)

        return ans