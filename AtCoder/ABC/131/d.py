# https://atcoder.jp/contests/abc131/tasks/abc131_d

import itertools
from collections import Counter
from collections import defaultdict
import bisect
from heapq import heappush, heappop

def main():
    N = int(input())
    AB = []
    for _ in range(N):
        a, b = map(int, input().split())
        AB.append((a, b))

    AB.sort(key=lambda x: x[1])

    possible = True
    current = 0
    for a, b in AB:
        current += a
        if current <= b:
            pass
        else:
            possible = False
            break

    print('Yes' if possible else 'No')


if __name__ == '__main__':
    main()
