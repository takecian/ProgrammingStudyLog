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
    dic = defaultdict(lambda: 0)
    count = 0
    for _ in range(n):
        s = input()
        dic[s] += 1
        count = max(count, dic[s])

    candidates = []
    for key in dic.keys():
        if dic[key] == count:
            candidates.append(key)

    candidates.sort()
    for c in candidates:
        print(c)

if __name__ == '__main__':
    main()
