# https://atcoder.jp/contests/abc091/tasks/abc091_b

import itertools
import collections
import bisect

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    sc = collections.Counter(S)
    M = int(input())
    T = [input() for _ in range(M)]
    tc = collections.Counter(T)

    ans = 0
    for item in sc.items():
        ans = max(ans, item[1] - tc[item[0]])
    print(ans)


if __name__ == '__main__':
    main()
