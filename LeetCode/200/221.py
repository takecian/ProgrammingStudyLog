class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        H = len(matrix)
        if H == 0:
            return 0
        W = len(matrix[0])
        if W == 0:
            return 0

        def calc_area(sy, sx):
            area = 0
            edge = 1
            while True:
                # top -> down
                y = sy
                x = sx + edge - 1
                if W <= x:
                    return area

                for i in range(edge):
                    if H <= y + i or matrix[y + i][x] != '1':
                        return area

                y = sy + edge - 1
                # right -> left
                for i in range(edge):
                    if matrix[y][x - i] != '1':
                        return area

                area = edge * edge
                edge += 1

            return area

        ans = 0
        for h in range(H):
            for w in range(W):
                if matrix[h][w] != '1':
                    continue
                ans = max(ans, calc_area(h, w))

        return ans


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        H = len(matrix)
        if H == 0:
            return 0
        W = len(matrix[0])
        if W == 0:
            return 0

        def calc_area(sy, sx):
            area = 0
            edge = 1
            while True:
                # top -> down
                y = sy
                x = sx + edge - 1
                if W <= x:
                    return area

                for i in range(edge):
                    if H <= y + i or matrix[y + i][x] != '1':
                        return area

                y = sy + edge - 1
                # right -> left
                for i in range(edge):
                    if matrix[y][x - i] != '1':
                        return area

                area = edge * edge
                edge += 1

            return area

        ans = 0
        for h in range(H):
            for w in range(W):
                if matrix[h][w] != '1':
                    continue
                ans = max(ans, calc_area(h, w))

        return ans
