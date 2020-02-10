import sys
sys.setrecursionlimit(12345678)
import itertools
from collections import Counter
from collections import defaultdict
from collections import deque
import bisect
from heapq import heappush, heappop


def main():
    ans = [1,2,3]
    a = int(input())
    b = int(input())
    ans.remove(a)
    ans.remove(b)
    print(ans.pop())

if __name__ == '__main__':
    main()
