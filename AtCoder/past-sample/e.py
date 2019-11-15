import sys
sys.setrecursionlimit(12345678)
import itertools
from collections import Counter
from collections import defaultdict
from collections import deque
import bisect
from heapq import heappush, heappop


def main():
    n, m = map(int, input().split())
    cl = [[int(i) for i in input().split()] + [j] for j in range(m)]

    # print(c_l)
    cl.sort(key=lambda x: x[1])

    counter = [0] * (n + 1)
    for c in cl:
        p = c[0]
        counter[p] += 1
        c.append("{:06}{:06}".format(c[0], counter[p]))

    cl.sort(key=lambda x: x[2])

    for c in cl:
        print(c[3])


if __name__ == '__main__':
    main()
