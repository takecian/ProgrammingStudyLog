# https://leetcode.com/problems/minimum-cost-to-hire-k-workers/

import itertools
from collections import Counter
from collections import defaultdict
import bisect
from heapq import heappush, heappop


class Solution:
    def mincostToHireWorkers(self, quality, wage, K: int) -> float:
        # choose captain
        ans = 10 ** 10
        workers = [(q, w) for q, w in zip(quality, wage)]
        for i in range(len(quality)):
            captain_q = workers[i][0]
            captain_w = workers[i][1]
            ratio = captain_w / captain_q  # 1 quality あたりの仕事量
            candi = list(filter(lambda x: x[1] / x[0] <= ratio, workers))
            candi = list(map(lambda x: max(x[1], x[0] * ratio), candi))
            # print(candi)
            candi.sort()
            if len(candi) < K:
                continue
            ans = min(ans, sum(candi[:K]))

        return ans


def main():
    s = Solution()
    print(s.mincostToHireWorkers([10,20,5],[70,50,30],2))
    print(s.mincostToHireWorkers([3,1,10,10,1],[4,8,2,2,7],3))

if __name__ == '__main__':
    main()
