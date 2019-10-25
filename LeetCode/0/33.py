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


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1

        sl = 0
        sr = len(nums) - 1
        if nums[0] > nums[-1]:
            l = 0
            r = len(nums) - 1
            while r - l > 1:
                m = (l + r) // 2
                if nums[l] < nums[m]:
                    l = m
                else:
                    r = m

            if nums[0] <= target:
                sr = l
            else:
                sl = r

        while sl <= sr:
            m = (sl + sr) // 2
            if nums[m] == target:
                return m
            if nums[m] < target:
                sl = m + 1
            else:
                sr = m - 1

        return -1
