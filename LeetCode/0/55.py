# https://leetcode.com/problems/jump-game/

import itertools
from collections import Counter
from collections import defaultdict
import bisect
from heapq import heappush, heappop


class Solution:
    def canJump(self, nums):
        top = 0
        for i in range(len(nums)):
            if top < i:
                return False
            top = max(top, i + nums[i])

        return True

def main():
    s = Solution()
    print(s.canJump([2,3,1,1,4]))
    print(s.canJump([3,2,1,0,4]))

if __name__ == '__main__':
    main()
