from collections import defaultdict
from heapq import heappush, heappop
from typing import List

def topKFrequent(nums: List[int], k: int) -> List[int]:
    counter = defaultdict(int)
    for n in nums:
        counter[n] += 1

    que = []
    for num, count in counter.items():
        heappush(que, (-count, num))

    ans = []
    c = len(que)
    for _ in range(c):
        count, num = heappop(que)
        ans.append(num)
    print(ans)
    return ans[k-1]

def solve2(nums: List[int], k: int) -> List[int]:
    counter = defaultdict(int)
    for n in nums:
        counter[n] += 1
    print(counter)
    print(counter.items())
    sorted_counter = sorted(counter.items(), key=lambda x:-x[1])
    print(sorted_counter)
    return sorted_counter[k-1][0]

print(topKFrequent(["John", "Kevin", "Kevin", "Bob", "Bob", "Bob"], 2))

print(solve2(["John", "Kevin", "Kevin", "Bob", "Bob", "Bob"], 2))

