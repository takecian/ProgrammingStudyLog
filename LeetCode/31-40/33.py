# https://leetcode.com/problems/search-in-rotated-sorted-array/

import itertools
from collections import Counter
import bisect


class Solution:
    def search(self, nums, target):
        l = 0
        r = len(nums) - 1
        while l <= r:
            # print("l = {}, r = {}".format(l, r))
            m = (l + r) >> 1
            if nums[m] == target:
                return m

            if nums[l] <= nums[m]:  # no ratate
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:  # rotated
                if nums[l] <= target or target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            # print("l = {}, r = {}".format(l, r))
        return -1


def main():
    s = Solution()
    # print(s.search([4,5,6,7,0,1,2], 3))
    # print(s.search([1], 1))
    # print(s.search([3, 1], 1))
    # print(s.search([5, 1, 3], 3))

    print(s.search([1, 3], 3))

if __name__ == '__main__':
    main()
