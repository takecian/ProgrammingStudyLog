# https://leetcode.com/problems/merge-intervals/

import itertools
from collections import Counter
from collections import defaultdict
import bisect
from heapq import heappush, heappop

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

def main():
    s = Solution()
    print(s.merge([[1,3],[2,6],[8,10],[15,18]]))

if __name__ == '__main__':
    main()
