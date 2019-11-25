# https://atcoder.jp/contests/abc146/tasks/abc146_a

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
    ans = 0
    if s == 'SUN':
        ans = 7
    if s == 'MON':
        ans = 6
    if s == 'TUE':
        ans = 5
    if s == 'WED':
        ans = 4
    if s == 'THU':
        ans = 3
    if s == 'FRI':
        ans = 2
    if s == 'SAT':
        ans = 1
    print(ans)

if __name__ == '__main__':
    main()
