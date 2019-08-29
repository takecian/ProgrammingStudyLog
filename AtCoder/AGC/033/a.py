import itertools
from collections import Counter
from collections import defaultdict
from collections import deque
import bisect


def main():
    H, W = map(int, input().split())
    A = [list(input()) for _ in range(H)]

    checked = [[False] * W for _ in range(H)]
    ans = 0

    que = []
    for h in range(H):
        for w in range(W):
            if A[h][w] == '#' and not checked[h][w]:
                que.append((h, w))
                checked[h][w] = True
    while que:
        next_que = []
        while que:
            h, w = que.pop()
            dx4 = [0, 0, 1, -1]
            dy4 = [1, -1, 0, 0]

            for dx, dy in zip(dx4, dy4):
                next_h = h + dy
                next_w = w + dx
                if 0 <= next_h < H and 0 <= next_w < W and A[next_h][next_w] == '.' and not checked[next_h][next_w]:
                    A[next_h][next_w] = '#'
                    checked[h][w] = True
                    next_que.append((next_h, next_w))
        que = next_que
        if que:
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()
