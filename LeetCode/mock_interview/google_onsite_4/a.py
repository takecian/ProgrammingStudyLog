class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        ans = ''

        def move(from_h, from_w, to_h, to_w):
            # print(from_h, from_w, to_h, to_w)
            nonlocal ans
            ans += 'L' * (from_w - to_w)
            ans += 'U' * (from_h - to_h)
            ans += 'D' * (to_h - from_h)
            ans += 'R' * (to_w - from_w)
            ans += '!'
            # ans += board[to_h][to_w]

        board = {c: [i // 5, i % 5] for i, c in enumerate("abcdefghijklmnopqrstuvwxyz")}

        h = 0
        w = 0
        for char in target:
            to_h, to_w = board[char]
            move(h, w, to_h, to_w)
            h = to_h
            w = to_w
        return ans