# https://atcoder.jp/contests/chokudai_S002/tasks/chokudai_S002_h
import itertools
from collections import Counter
from collections import defaultdict
import bisect
from heapq import heappush, heappop

def main():
    N = int(input())
    for _ in range(N):
        a, b = map(int, input().split())
        print(-1 if a == b else abs(a - b))


if __name__ == '__main__':
    main()
