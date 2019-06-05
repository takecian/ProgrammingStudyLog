
import itertools
from collections import Counter
from collections import defaultdict
import bisect
from heapq import heappush, heappop

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        nums1.sort()
        nums2.sort()
        c1 = nums1[:k]
        c2 = nums2[:k]
        cand = [(a, b, a + b) for a, b in itertools.product(c1, c2)]
        # print(cand)
        cand.sort(key=lambda x: x[2])
        ans = list(map(lambda x: [x[0], x[1]], cand))
        return ans[:k]


def main():
    s = Solution()
    print(s.kSmallestPairs([1,7,11], [2,4,6]))

if __name__ == '__main__':
    main()
