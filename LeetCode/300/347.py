from collections import defaultdict
from heapq import heappush, heappop


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        for n in nums:
            counter[n] += 1

        que = []
        for num, count in counter.items():
            heappush(que, (-count, num))

        ans = []
        for _ in range(k):
            count, num = heappop(que)
            ans.append(num)
        return ans
