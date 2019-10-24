# bisect

import bisect

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        nums.sort()
        self.nums = nums

    def add(self, val: int) -> int:
        pos = bisect.bisect(self.nums, val)
        # print('a',self.nums)
        if pos == len(self.nums):
            self.nums.append(val)
        else:
            self.nums.insert(pos, val)

        if len(self.nums) > self.k:
            self.nums = self.nums[len(self.nums) - self.k:]

        # print('b',self.nums)
        return self.nums[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

#  heapq approach
import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.que = nums
        heapq.heapify(self.que)

    def add(self, val: int) -> int:
        heapq.heappush(self.que, val)

        while len(self.que) > self.k:
            heapq.heappop(self.que)

        return self.que[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)