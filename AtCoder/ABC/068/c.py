# https://atcoder.jp/contests/abc068/tasks/arc079_a

import itertools
from collections import Counter
from collections import defaultdict
import bisect

def main():
    N, M = map(int, input().split())
    s_list = []
    g_list = []

    for _ in range(M):
        a, b = map(int, input().split())
        if a == 1:
            s_list.append(b)
        if b == N:
            g_list.append(a)

    for s in s_list:
        if s in g_list:
            print("POSSIBLE")
            exit()
    print("IMPOSSIBLE")


if __name__ == '__main__':
    main()
