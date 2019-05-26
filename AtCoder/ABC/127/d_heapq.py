# https://atcoder.jp/contests/abc127/tasks/abc127_d


import itertools
from collections import Counter
from collections import defaultdict
import bisect
from heapq import heappush, heappop

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    heap = []
    for a in A:
        heappush(heap, (-a, 1))

    for _ in range(M):
        b, c = map(int, input().split())
        heappush(heap, (-c, b))

    cards = []
    while len(cards) < N:
        val, num = heappop(heap)
        cards.append(-val)
        if num > 1:
            heappush(heap, (val, num - 1))

    print(sum(cards))

if __name__ == '__main__':
    main()
