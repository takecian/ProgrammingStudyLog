class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        A.sort()
        i = 0
        j = len(A) - 1
        ans = -1
        while i < j:
            if A[i] + A[j] < K:
                ans = max(ans, A[i] + A[j])
                i += 1
            else:
                j -= 1
        return ans if ans != -1 else -1