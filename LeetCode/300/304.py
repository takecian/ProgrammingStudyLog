class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        H = len(self.matrix)
        if H > 0:
            W = len(self.matrix[0])
            if H > 1:
                for h in range(H - 1):
                    for w in range(W):
                        self.matrix[h + 1][w] += self.matrix[h][w]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row3 = row2
        col3 = col1
        row4 = row1
        col4 = col2
        area = 0
        for c in range(col1, col2 + 1):
            if row1 == 0:
                area += self.matrix[row2][c]
            else:
                area += (self.matrix[row2][c] - self.matrix[row1 - 1][c])
        return area