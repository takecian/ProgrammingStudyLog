# https://leetcode.com/problems/permutations/

import itertools
from collections import Counter
import bisect


class Solution:
    def permute(self, nums):
        ans = []
        for l in itertools.permutations(nums):
            ans.append(list(l))
        return ans


def main():
    s = Solution()
    s.permute([1,2,3])

if __name__ == '__main__':
    main()
