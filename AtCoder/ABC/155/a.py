# https://atcoder.jp/contests/abc155/tasks/abc155_a
import sys
sys.setrecursionlimit(12345678)
import itertools
from collections import Counter
from collections import defaultdict
from collections import deque
import bisect
from heapq import heappush, heappop


def main():
    a, b, c = map(int, input().split())
    if a != b and b != c and c != a:
        print('No')
        return
    if a == b and b == c and c == a:
        print('No')
        return

    print('Yes')
    return


if __name__ == '__main__':
    main()
