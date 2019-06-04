# https://leetcode.com/problems/merge-intervals/

import itertools
from collections import Counter
from collections import defaultdict
import bisect
from heapq import heappush, heappop


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        i = 0
        while i < len(intervals):
            b = intervals[i]
            start = b[0]
            end = b[1]
            j = i + 1
            while j < len(intervals):
                ne = intervals[j]
                if end <= ne[0]:
                    end = max(end, ne[1])
                    i = j
                    j += 1
                else:
                    break
            ans.append([start, end])

        return ans

def main():
    s = Solution()
    print(s.merge([[1,4],[4,5]]))

if __name__ == '__main__':
    main()
