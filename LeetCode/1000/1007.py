aclass Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        n = len(A)

        ans = 10**10
        for i in [A[0],B[0]]:
            can_be_same = True
            a_count = 0
            b_count = 0
            for j in range(n):
                if A[j] != i and B[j] != i:
                    can_be_same = False
                    break
                if A[j] == i and B[j] != i:
                    a_count += 1
                if A[j] != i and B[j] == i:
                    b_count += 1
            if can_be_same:
                ans = min(ans, a_count, b_count)
        return ans if ans !=  10**10 else -1