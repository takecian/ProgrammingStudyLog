class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        return matrix and list(matrix.pop(0)) + self.spiralOrder(zip(*matrix)[::-1])


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        def rotate(matrix):
            if not matrix or not matrix[0]:
                return []
            new_matrix = []
            # inverse
            H = len(matrix)
            W = len(matrix[0])

            for w in range(W):
                row = [matrix[h][w] for h in range(H)]
                new_matrix.append(row)
            # reverse
            new_matrix.reverse()
            return new_matrix

        ans = []
        while matrix and matrix[0]:
            row = matrix.pop(0)
            ans.extend(row)
            matrix = rotate(matrix)

        return ans
