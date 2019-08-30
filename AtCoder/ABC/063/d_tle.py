# https://atcoder.jp/contests/abc063/tasks/arc075_b
import sys
sys.setrecursionlimit(12345678)
import itertools
from collections import Counter
from collections import defaultdict
from collections import deque
import bisect
from heapq import heappush, heappop


def main():
    n, a, b = map(int, input().split())
    heap = []
    for _ in range(n):
        heappush(heap, -int(input()))

    ans = 0
    while True:
        strong_monster = heappop(heap)
        if strong_monster >= 0:
            break
        strong_monster += a
        for i in range(len(heap)):
            heap[i] += b
        heappush(heap, strong_monster)
        ans += 1
    print(ans)


if __name__ == '__main__':
    main()
