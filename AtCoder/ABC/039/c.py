# https://atcoder.jp/contests/abc039/tasks/abc039_c
import sys
sys.setrecursionlimit(12345678)
import itertools
from collections import Counter
from collections import defaultdict
from collections import deque
import bisect
from heapq import heappush, heappop


def main():
    s = input()

    do_si = "WBWBWWBWBWBW" * 3
    i = do_si.index(s)

    ans = {0: "Do",
           2: "Re",
           4: "Mi",
           5: "Fa",
           7: "So",
           9: "La",
           11: "Si"
           }

    print(ans[i])

if __name__ == '__main__':
    main()

