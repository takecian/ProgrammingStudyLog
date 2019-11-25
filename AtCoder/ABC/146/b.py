# https://atcoder.jp/contests/abc146/tasks/abc146_b

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
    s = input()
    base = ord('A')
    ans = ''
    for c in s:
        code = ord(c) - base
        replaced = chr((code + n) % 26 + base)
        ans += replaced
    print(ans)

if __name__ == '__main__':
    main()
