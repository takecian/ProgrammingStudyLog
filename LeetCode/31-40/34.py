# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/


import itertools
import collections
import bisect


class Solution:
    def searchRange(self, nums, target):
        r = bisect.bisect_right(nums, target)
        l = bisect.bisect_left(nums, target)
        if l == len(nums) or nums[l] != target:
            return [-1, -1]
        else:
            return [l, r - 1]

def main():
    s = Solution()
    print(s.searchRange([5,7,7,8,8,10], 8))
    print(s.searchRange([5,7,7,8,8,10], 6))

if __name__ == '__main__':
    main()
