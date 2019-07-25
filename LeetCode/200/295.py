# https://leetcode.com/problems/find-median-from-data-stream/

import bisect

class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.array = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        pos = bisect.bisect(self.array, num)
        self.array.insert(pos, num)

    def findMedian(self):
        """
        :rtype: float
        """
        n = len(self.array)
        if n == 0:
            return 0

        if n % 2 == 1:
            return self.array[n // 2]
        else:
            return (self.array[n // 2 - 1] + self.array[n // 2]) / 2.0

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()