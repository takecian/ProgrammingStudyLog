class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        0 is dead
        1 is live,
        2 is current dead, next live
        3 is current live, next live
        4 is current dead, next dead
        5 is current live, next dead
        """
        if len(board) == 0 or len(board[0]) == 0:
            return
        H = len(board)
        W = len(board[0])

        def next_state(h, w):
            live_count = 0
            dead_count = 0
            current = board[h][w]  # 0 or 1
            for dh, dw in zip([-1, -1, -1, 0, 0, 1, 1, 1], [-1, 0, 1, -1, 1, -1, 0, 1]):
                next_h = h + dh
                next_w = w + dw
                if 0 <= next_h < H and 0 <= next_w < W:
                    if board[next_h][next_w] % 2 == 0:
                        dead_count += 1
                    else:
                        live_count += 1
            if current == 1:
                if live_count == 2 or live_count == 3:
                    return 3
                else:
                    return 5
            else:
                return 2 if live_count == 3 else 4

        for h in range(H):
            for w in range(W):
                board[h][w] = next_state(h, w)

        for h in range(H):
            for w in range(W):
                board[h][w] = 1 if board[h][w] == 2 or board[h][w] == 3 else 0

