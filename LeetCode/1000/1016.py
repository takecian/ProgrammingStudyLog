class Solution:
    def queryString(self, S: str, N: int) -> bool:
        for i in range(N, N // 2, -1):
            if not bin(i)[2:] in S:
                return False
        return True