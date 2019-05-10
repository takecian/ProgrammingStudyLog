class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        height = len(matrix)
        width = len(matrix[0])

        offset = 0
        while height > 0 and width > 0:
            # to right
            for i in range(width - offset - 1):
                matrix[offset][i]

            # to bottom
            for i in range(height - offset - 1):
                matrix[i][width - 1 - offset]
            # to left
            for i in range(width - offset - 1, offset, -1):
                matrix[height - 1 - offset][i]

            # to up
            for i in range(height - offset - 1, offset, -1):
                matrix[i][offset]

            offset += 1
