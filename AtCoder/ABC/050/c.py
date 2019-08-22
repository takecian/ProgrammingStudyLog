# https://atcoder.jp/contests/abc050/tasks/arc066_a
import sys
sys.setrecursionlimit(12345678)
import itertools
from collections import Counter
from collections import defaultdict
from collections import deque
import bisect
from heapq import heappush, heappop


def main():
    n = int(input())
    al = list(map(int, input().split()))
    al.sort()

    if len(al) % 2 == 1:  # odd
        if al[0] != 0:
            print(0)
            return
        al = al[1:]

    for i in range(0, len(al), 2):
        if al[i] != al[i+1]:
            print(0)
            return

    mod = 10**9 + 7
    print(2 ** (len(al) // 2) % mod)


if __name__ == '__main__':
    main()
