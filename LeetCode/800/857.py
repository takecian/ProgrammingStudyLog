# https://leetcode.com/problems/minimum-cost-to-hire-k-workers/

import itertools
from collections import Counter
from collections import defaultdict
import bisect
from heapq import heappush, heappop


class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        workers = [[float(w) / q, q] for w, q in zip(wage, quality)]
        workers.sort()  # 1quality あたりのコストでソート
        ans = float('inf')
        qsum = 0
        heap = []
        for r, q in workers:  # 1quality あたりの少ない方から追加していく、 ratio が小さいものは条件2を満たさないため
            if len(heap) == K:
                qsum += heappop(heap)  # いっぱいだったら quality の大きいものを除外する、不要なので

            heappush(heap, -q)
            qsum += q
            if len(heap) == K:
                ans = min(ans, qsum * r)

        return ans


def main():
    s = Solution()
    print(s.mincostToHireWorkers([10,20,5],[70,50,30],2))
    print(s.mincostToHireWorkers([3,1,10,10,1],[4,8,2,2,7],3))

if __name__ == '__main__':
    main()
