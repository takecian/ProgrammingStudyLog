class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rotated = list(zip(*matrix[::-1]))
        n = len(matrix)
        for i in range(n):
            for j in range(n):
                matrix[i][j] = rotated[i][j]