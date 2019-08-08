class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        ans = []
        for s, e in intervals:
            if len(ans) == 0:
                ans.append([s,e])
            else:
                if s <= ans[-1][1]:
                    ans[-1][1] = max(ans[-1][1], e)
                else:
                    ans.append([s,e])
        return ans