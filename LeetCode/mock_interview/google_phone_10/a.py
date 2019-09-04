class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        n = len(A)
        if n < 3:
            return False
        i = 0
        prev = -1
        while i < n:
            if prev >= A[i]:
                break
            prev = A[i]
            i += 1
        if i == 1 or i == n:
            return False

        while i < n:
            if prev <= A[i]:
                break
            prev = A[i]
            i += 1
        return i == n
