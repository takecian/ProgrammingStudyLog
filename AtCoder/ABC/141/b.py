# https://atcoder.jp/contests/abc141/tasks/abc141_b
import sys
sys.setrecursionlimit(12345678)
import itertools
from collections import Counter
from collections import defaultdict
from collections import deque
import bisect
from heapq import heappush, heappop


def main():
    s = input()
    for i in range(len(s)):
        num = i + 1
        if num % 2 == 1:
            # odd
            if s[i] not in 'RUD':
                print('No')
                return
        else:
            # even
            if s[i] not in 'LUD':
                print('No')
                return

    print('Yes')

if __name__ == '__main__':
    main()
