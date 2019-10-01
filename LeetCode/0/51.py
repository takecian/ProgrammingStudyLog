class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['' for _ in range(n)] for _ in range(n)]
        ans = []

        def can_put(h, w):
            if queen_row[h] == 1:
                return False
            if h + w in upright:
                return False
            if h - w in downright:
                return False
            return True

        def put(h, w):
            queens.add((h, w))
            queen_row[h] = 1
            upright.add(h + w)
            downright.add(h - w)

        def remove(h, w):
            queens.remove((h, w))
            queen_row[h] = 0
            upright.remove(h + w)
            downright.remove(h - w)

        def backtrack(w):
            nonlocal ans
            if len(queens) == n:
                solution = [['' for _ in range(n)] for _ in range(n)]
                for h in range(n):
                    for w in range(n):
                        if (h, w) in queens:
                            solution[h][w] = 'Q'
                solution = [''.join(solution[h]) for h in range(n)]
                ans.append(solution)
                return

            for h in range(n):
                if can_put(h, w):
                    put(h, w)
                    backtrack(w + 1)
                    remove(h, w)

        queens = set()
        queen_row = [0] * n
        upright = set()
        downright = set()
        backtrack(0)
        return ans
