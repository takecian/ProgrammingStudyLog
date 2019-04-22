# https://leetcode.com/problems/maximum-subarray/

import itertools
import collections
import bisect


class Solution:
    def maxSubArray(self, nums):
        ans = nums[0]
        current_sum = 0
        for i in range(len(nums)):
            current_sum += nums[i]
            if current_sum > ans:
                ans = current_sum
            if current_sum < 0:
                current_sum = 0
        return ans


def main():
    s = Solution()
    # print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
    print(s.maxSubArray([-2,-1]))

if __name__ == '__main__':
    main()
