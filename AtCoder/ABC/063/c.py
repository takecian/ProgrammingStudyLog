# https://atcoder.jp/contests/abc063/tasks/arc075_a

import itertools
import collections
import bisect

def main():
    N = int(input())
    scores = []
    for _ in range(N):
        s = int(input())
        scores.append(s)

    ans = 0
    if sum(scores) % 10 != 0:
        ans = sum(scores)
    else:
        scores.sort()
        for c in scores:
            if c % 10 != 0:
                ans = sum(scores) - c
                break

    print(ans)

if __name__ == '__main__':
    main()
