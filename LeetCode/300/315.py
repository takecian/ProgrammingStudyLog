import itertools
from collections import Counter
from collections import defaultdict
import bisect
from heapq import heappush, heappop

class Solution:
    def countSmaller(self, nums):
        check = []
        ans = [0] * len(nums)
        for i in range(len(nums)-1, -1, -1):
            index = bisect.bisect_left(check, nums[i])
            ans[i] = index
            check.insert(index, nums[i])
        return ans

def main():
    s = Solution()
    print(s.countSmaller([5, 2, 6, 1]))


if __name__ == '__main__':
    main()
