# https://atcoder.jp/contests/abc119/tasks/abc119_c
import itertools
import collections
from bisect import bisect



def main():
    N, A, B, C = map(int, input().split())
    L = [int(input()) for _ in range(N)]

    def solve(i, a, b, c):
        if i == N:
            # 最初の追加は合成じゃないので +10 * 3(A,B,Cの分)が余分なので除外する
            # 最低でも１本使わないとダメ
            return abs(A-a) + abs(B-b) + abs(C-c) - 30 if min(a, b, c) > 0 else int(1e15)
        ret0 = solve(i + 1, a, b, c)
        ret1 = solve(i + 1, a + L[i], b, c) + 10
        ret2 = solve(i + 1, a, b + L[i], c) + 10
        ret3 = solve(i + 1, a, b, c + L[i]) + 10
        return min(ret0, ret1, ret2, ret3)

    print(solve(0, 0, 0, 0))


if __name__ == '__main__':
    main()
