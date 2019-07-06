# https://leetcode.com/problems/subarray-sum-equals-k/

import itertools
from collections import Counter
from collections import defaultdict
from collections import deque
import bisect
from heapq import heappush, heappop

from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cumulative = [0] * (len(nums) + 1)

        cumulative_map = defaultdict(lambda: 0)
        cumulative_map[0] = 1

        ans = 0
        for i in range(len(nums)):
            cumulative[i + 1] = nums[i] + cumulative[i]
            ans += cumulative_map[cumulative[i + 1] - k]
            cumulative_map[cumulative[i + 1]] += 1

        return ans


def main():
    s = Solution()
    print(s.subarraySum([1,1,1], 2))

if __name__ == '__main__':
    main()
