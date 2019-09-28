# https://atcoder.jp/contests/abc142/tasks/abc142_c
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
    al = [(i, a) for i, a in enumerate(al)]
    al.sort(key=lambda a: a[1])
    al = [i + 1 for i, a in al]
    print(' '.join(map(str, al)))


if __name__ == '__main__':
    main()
