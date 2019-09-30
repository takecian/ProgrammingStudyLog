class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['' for _ in range(n)] for _ in range(n)]
        ans = []

        def can_put(h, w):
            # right top
            ch = h
            cw = w
            while 0 <= ch and cw < n:
                if board[ch][cw] == 'Q':
                    return False
                ch -= 1
                cw += 1
            # left top
            ch = h
            cw = w
            while 0 <= ch and 0 <= cw:
                if board[ch][cw] == 'Q':
                    return False
                ch -= 1
                cw -= 1
            # right down
            ch = h
            cw = w
            while ch < n and cw < n:
                if board[ch][cw] == 'Q':
                    return False
                ch += 1
                cw += 1
            # left down
            ch = h
            cw = w
            while ch < n and 0 <= cw:
                if board[ch][cw] == 'Q':
                    return False
                ch += 1
                cw -= 1
            return True

        def put(h, w):
            # right top
            ch = h
            cw = w
            while 0 <= ch and cw < n:
                board[ch][cw] = 'Q'
                ch -= 1
                cw += 1
            # left top
            ch = h
            cw = w
            while 0 <= ch and 0 <= cw:
                board[ch][cw] = 'Q'
                ch -= 1
                cw -= 1
            # right down
            ch = h
            cw = w
            while ch < n and cw < n:
                board[ch][cw] = 'Q'
                ch += 1
                cw += 1
            # left down
            ch = h
            cw = w
            while ch < n and 0 <= cw:
                board[ch][cw] = 'Q'
                ch += 1
                cw -= 1

        def remove(h, w):
            # right top
            ch = h
            cw = w
            while 0 <= ch and cw < n:
                board[ch][cw] = ''
                ch -= 1
                cw += 1
            # left top
            ch = h
            cw = w
            while 0 <= ch and 0 <= cw:
                board[ch][cw] = ''
                ch -= 1
                cw -= 1
            # right down
            ch = h
            cw = w
            while ch < n and cw < n:
                board[ch][cw] = ''
                ch += 1
                cw += 1
            # left down
            ch = h
            cw = w
            while ch < n and 0 <= cw:
                board[ch][cw] = ''
                ch += 1
                cw -= 1
            return True

        def backtrack(w):
            nonlocal ans
            print(w, board)
            if w == n - 1:
                yeah = [[board[ph][pw] for pw in range(n)] for ph in range(n)]
                ans.append(yeah)
                return
            for h in range(n):
                if can_put(h, w):
                    put(h, w)
                    backtrack(w + 1)
                    remove(h, w)

        backtrack(0)
        return ans
