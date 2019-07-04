class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        A = list(map(lambda x: x * x, A))
        A.sort()
        return A
