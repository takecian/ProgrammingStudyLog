# https://atcoder.jp/contests/abc060/tasks/arc073_a

import itertools
import collections
import bisect

def main():
    N, T = map(int, input().split())
    ts = list(map(int, input().split()))

    ans = 0

    for i in range(1, len(ts)):
        ans += min(T, ts[i] - ts[i-1])
    ans += T
    print(ans)


if __name__ == '__main__':
    main()
