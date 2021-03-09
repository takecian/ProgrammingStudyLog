import sys
sys.setrecursionlimit(12345678)
import itertools
from collections import Counter
from collections import defaultdict
from collections import deque
import bisect
from heapq import heappush, heappop

class Solution:
    def runningSum(self, nums):
        ans = []
        for num in nums:
            if len(ans) == 0:
                ans.append(num)
            else:
                ans.append(num + ans[-1])
        return ans

def main():
    s = Solution()
    print(s.runningSum([1,2,3,4]))


if __name__ == '__main__':
    main()
