# https://atcoder.jp/contests/abc082/tasks/arc087_a

import itertools
import collections
import bisect
import sys
input = sys.stdin.readline

def main():
    N = int(input())
    A = list(map(int, input().split()))
    c = collections.Counter(A)

    ans = 0
    for k, v in c.items():
        if k > v:  # 数が足りないなら取り除く
            ans += v
        else:
            ans += v - k
    print(ans)

if __name__ == '__main__':
    main()
