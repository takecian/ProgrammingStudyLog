class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        prev = None
        for i in range(len(A)):
            if prev is None:
                prev = A[i]
            else:
                if prev > A[i]:
                    return i - 1
                prev = A[i]