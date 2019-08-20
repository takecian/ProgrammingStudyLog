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
    sara = defaultdict(list)
    for i in range(n-1):
        val = int(input())
        val -= 1
        sara[val].append(i+1)

    cache = {}

    def calc(i):
        if i in cache:
            return cache[i]
        if len(sara[i]) == 0:
            cache[i] = 1
            return cache[i]
        max_sara = 0
        min_sara = 10**10
        for s in sara[i]:
            max_sara = max(max_sara, calc(s))
            min_sara = min(min_sara, calc(s))

        cache[i] = max_sara + min_sara + 1
        return cache[i]

    print(calc(0))


if __name__ == '__main__':
    main()
