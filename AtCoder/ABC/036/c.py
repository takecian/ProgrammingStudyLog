# https://atcoder.jp/contests/abc036/tasks/abc036_c

import itertools
from collections import Counter
from collections import defaultdict
from collections import deque
import bisect
from heapq import heappush, heappop

def main():
    n = int(input())
    al = []
    bl = []
    for _ in range(n):
        a = int(input())
        al.append(a)

    bl = list(set(al))
    bl.sort()
    conv = {}
    for i in range(len(bl)):
        conv[bl[i]] = i

    for i in range(len(al)):
        print(conv[al[i]])


if __name__ == '__main__':
    main()
