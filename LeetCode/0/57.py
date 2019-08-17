class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        ans = []
        for s, e in intervals:
            if len(ans) == 0:
                ans.append([s, e])
            else:
                if s <= ans[-1][1]:
                    ans[-1][1] = max(ans[-1][1], e)
                else:
                    ans.append([s, e])
        return ans

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])

        return self.merge(intervals)