class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0]:
            return False
        if len(word) == 0:
            return True

        H = len(board)
        W = len(board[0])

        def find(h, w, target):
            if len(target) == 0:
                return True
            if h < 0 or H == h or w < 0 or W == w:
                return False
            if board[h][w] != target[0]:
                return False

            board[h][w] = ''
            for dh, dw in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                next_h = h + dh
                next_w = w + dw
                if find(next_h, next_w, target[1:]):
                    return True

            board[h][w] = target[0]
            return False

        for h in range(H):
            for w in range(W):
                if find(h, w, word):
                    return True

        return False
