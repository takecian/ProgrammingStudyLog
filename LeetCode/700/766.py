class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        h = len(matrix)
        w = len(matrix[0])

        # top -> right
        for i in range(w):
            target = matrix[0][i]
            for j in range(h):
                val = matrix[j][i + j]
                if target != val:
                    return False
                if i + j == w - 1:
                    break

        # top -> down
        for i in range(h):
            target = matrix[i][0]
            for j in range(w):
                val = matrix[i + j][j]
                if target != val:
                    return False
                if i + j == h - 1:
                    break
        return True