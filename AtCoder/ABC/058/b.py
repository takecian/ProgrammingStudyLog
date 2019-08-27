# https://atcoder.jp/contests/abc058/tasks/abc058_b
import sys
sys.setrecursionlimit(12345678)
import itertools
from collections import Counter
from collections import defaultdict
from collections import deque
import bisect
from heapq import heappush, heappop


def main():
    o = input()
    e = input()
    ans = ''
    for i in range(len(o)):
        ans += o[i]
        if i < len(e):
            ans += e[i]

    print(ans)


if __name__ == '__main__':
    main()
