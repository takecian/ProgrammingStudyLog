class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)

        big_int = 10 ** 10
        for i in range(1, n):
            pre1 = [big_int] + triangle[i - 1]
            pre2 = triangle[i - 1] + [big_int]
            for j in range(len(triangle[i])):
                triangle[i][j] = min(triangle[i][j] + pre1[j], triangle[i][j] + pre2[j])

        return min(triangle[-1])

