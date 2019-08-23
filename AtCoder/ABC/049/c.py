# https://atcoder.jp/contests/abc049/tasks/arc065_a
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
    possible = [False] * (len(s) + 1)
    possible[0] = True

    candidates = ['dream', 'dreamer', 'erase', 'eraser']
    for i in range(len(s)):
        if not possible[i]:
            continue
        for c in candidates:
            if s[i:i+len(c)] == c:
                possible[i + len(c)] = True

    print('YES' if possible[-1] else 'NO')


if __name__ == '__main__':
    main()
