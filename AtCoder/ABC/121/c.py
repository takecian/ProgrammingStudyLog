# https://atcoder.jp/contests/abc121/tasks/abc121_c

import itertools
import collections
import bisect

def main():
    N, M = map(int, input().split())
    AB = []
    for _ in range(N):
        a, b = map(int, input().split())
        AB.append((a, b))
    AB.sort(key=lambda x:x[0])
    # print(AB)

    ans = 0
    rest = M

    for ab in AB:
        buy_count = min(rest, ab[1])
        ans += ab[0] * buy_count
        rest -= buy_count
        if rest == 0:
            break
    print(ans)


if __name__ == '__main__':
    main()
