class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        val = 1
        offset = 0
        while True:
            h = offset
            w = offset
            # right
            while w < n - offset:
                matrix[h][w] = val
                w += 1
                val += 1
            w -= 1
            if n == offset * 2 + 1:
                break
            h += 1
            # down
            while h < n - offset:
                matrix[h][w] = val
                h += 1
                val += 1
            h -= 1
            w -= 1

            # left
            while offset - 1 < w:
                matrix[h][w] = val
                w -= 1
                val += 1
            w += 1
            h -= 1
            if n == offset * 2 + 2:
                break

            # up
            while offset < h:
                matrix[h][w] = val
                h -= 1
                val += 1
            offset += 1
        return matrix