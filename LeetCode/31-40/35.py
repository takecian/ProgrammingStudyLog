# https://leetcode.com/problems/search-insert-position/

import itertools
from collections import Counter
import bisect


class Solution:
    def searchInsert(self, nums, target):
        return bisect.bisect_left(nums, target)

def main():
    s = Solution()
    print(s.searchInsert([1,3,5,6], 2))

if __name__ == '__main__':
    main()
