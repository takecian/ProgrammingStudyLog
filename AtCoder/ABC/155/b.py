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

    for a in al:
        if a % 2 == 1:
            continue
        if a % 3 == 0:
            continue
        if a % 5 == 0:
            continue

        print('DENIED')
        return

    print('APPROVED')
    return

if __name__ == '__main__':
    main()
