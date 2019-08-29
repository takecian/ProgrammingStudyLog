
class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        if N == 1:
            return 0
        if N == 2:
            return K - 1
        if 2 ** (N-2) < K:
            ret = self.kthGrammar(N-1, K - 2 ** (N-2))
            return 1 if ret == 0 else 0
        else:
            return self.kthGrammar(N-1, K)

