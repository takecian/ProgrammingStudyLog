import itertools
from collections import Counter
from collections import defaultdict
from collections import deque
import bisect


def main():
    H, W = map(int, input().split())
    A = [list(input()) for _ in range(H)]
    # big value
    INF = int(1e15)
    distance = [[INF] * W for _ in range(H)]

    for h in range(H):
        for w in range(W):
            if A[h][w] == '#':
                distance[h][w] = 0

    for h in range(H):
        for w in range(W-1):
            distance[h][w + 1] = min(distance[h][w + 1], distance[h][w] + 1)
        for w in range(W - 1, 0, -1):
            distance[h][w - 1] = min(distance[h][w - 1], distance[h][w] + 1)

    for w in range(W):
        for h in range(H-1):
            distance[h + 1][w] = min(distance[h + 1][w], distance[h][w] + 1)
        for h in range(H - 1, 0, -1):
            distance[h - 1][w] = min(distance[h - 1][w], distance[h][w] + 1)

    ans = 0
    # print(distance)
    for h in range(H):
        ans = max(ans, max(distance[h]))

    print(ans)


if __name__ == '__main__':
    main()
