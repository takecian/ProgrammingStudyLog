import sys
sys.setrecursionlimit(12345678)
import itertools
from collections import Counter
from collections import defaultdict
from collections import deque
from typing import List
import bisect
from heapq import heappush, heappop

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        greatest_num = max(candies)
        ans = []
        for candy in candies:
            if greatest_num <= candy + extraCandies:
                ans.append(True)
            else:
                ans.append(False)
        return ans


def main():
    s = Solution()
    print(s.kidsWithCandies([2,3,5,1,3], 3))

if __name__ == '__main__':
    main()
