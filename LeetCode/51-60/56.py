# https://leetcode.com/problems/merge-intervals/

import itertools
from collections import Counter
from collections import defaultdict
import bisect
from heapq import heappush, heappop


class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])
        ans = []
        i = 0
        while i < len(intervals):
            b = intervals[i]
            # print(b)
            start = b[0]
            end = b[1]
            j = i + 1
            while j < len(intervals):
                ne = intervals[j]
                # print(ne)
                if ne[0] <= end:
                    end = max(end, ne[1])
                    j += 1
                    i = j
                else:
                    i = j
                    break
            ans.append([start, end])
            if j == len(intervals):
                break

        return ans

def main():
    s = Solution()
    print(s.merge([[1,3],[2,6],[8,10],[15,18]]))

if __name__ == '__main__':
    main()
