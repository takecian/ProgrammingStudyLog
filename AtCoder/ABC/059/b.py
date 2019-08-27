import sys
sys.setrecursionlimit(12345678)
import itertools
from collections import Counter
from collections import defaultdict
from collections import deque
import bisect
from heapq import heappush, heappop
# https://atcoder.jp/contests/abc059/tasks/abc059_b

def main():
    a = int(input())
    b = int(input())
    if a > b:
        print('GREATER')
        return
    if a < b:
        print('LESS')
        return

    print('EQUAL')


if __name__ == '__main__':
    main()
